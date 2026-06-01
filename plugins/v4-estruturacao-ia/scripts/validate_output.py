"""
validate_output.py — Valida completude de outputs de skill contra seu JSON Schema.

Objetivo: garantir que toda skill gere outputs com TODOS os campos preenchidos.
Quando o dado nao pode ser obtido, o output deve usar null + unavailable_reason
no objeto pai (ver shared-templates/PADRAO-OUTPUT.md).

Uso:
    python3 validate_output.py <client_dir>
    python3 validate_output.py <client_dir> --skill ee-s2-diagnostico-cro
    python3 validate_output.py <client_dir> --strict   # exit != 0 se houver warnings

Saida: relatorio legivel em stdout. Exit 0 salvo em --strict com findings.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
SKILLS_DIR = SCRIPT_DIR.parent / "skills"


def load_schema(skill_id: str) -> dict | None:
    schema_path = SKILLS_DIR / skill_id / "schema.json"
    if not schema_path.exists():
        return None
    with schema_path.open(encoding="utf-8") as f:
        return json.load(f)


def siblings_have_unavailable_reason(parent: Any, field: str) -> bool:
    """Checa se o objeto pai tem algum campo que justifica o null/vazio."""
    if not isinstance(parent, dict):
        return False
    markers = (
        "unavailable_reason",
        f"{field}_note",
        f"{field}_reason",
        "notes",
        "note",
        "data_source",
        "estimated",
        "honesty_alert",
    )
    for m in markers:
        if m in parent and parent[m] not in (None, "", []):
            return True
    return False


def walk(node: Any, schema: dict, path: str, findings: list[dict]) -> None:
    """Walk output + schema juntos. Reporta missing/null/vazio sem reason."""
    if not isinstance(schema, dict):
        return

    schema_type = schema.get("type")

    # Object: check required + properties
    if schema_type == "object" or "properties" in schema:
        if not isinstance(node, dict):
            if node is None:
                # Objeto nulo — precisa de reason em algum ancestral, mas aqui só loga
                findings.append({
                    "severity": "warn",
                    "path": path,
                    "kind": "null_object",
                    "message": "Objeto inteiro é null. Considere preencher ou marcar unavailable_reason no pai.",
                })
            return

        required = schema.get("required") or []
        props = schema.get("properties") or {}

        for req in required:
            if req not in node:
                findings.append({
                    "severity": "error",
                    "path": f"{path}.{req}" if path else req,
                    "kind": "missing_required",
                    "message": f"Campo obrigatório ausente.",
                })

        for key, sub_schema in props.items():
            if key not in node:
                continue
            sub_path = f"{path}.{key}" if path else key
            value = node[key]

            # Null check
            if value is None:
                if not siblings_have_unavailable_reason(node, key):
                    findings.append({
                        "severity": "warn",
                        "path": sub_path,
                        "kind": "null_without_reason",
                        "message": "Campo é null sem unavailable_reason/note no objeto pai.",
                    })
                continue

            # Empty string
            if isinstance(value, str) and value.strip() == "":
                findings.append({
                    "severity": "warn",
                    "path": sub_path,
                    "kind": "empty_string",
                    "message": "String vazia. Use null + unavailable_reason quando o dado não existe.",
                })
                continue

            walk(value, sub_schema, sub_path, findings)
        return

    # Array: check items
    if schema_type == "array":
        if not isinstance(node, list):
            return
        item_schema = schema.get("items") or {}
        min_items = schema.get("minItems")
        if min_items and len(node) < min_items:
            findings.append({
                "severity": "warn",
                "path": path,
                "kind": "array_too_short",
                "message": f"Array tem {len(node)} itens, mínimo {min_items}.",
            })
        if len(node) == 0:
            findings.append({
                "severity": "info",
                "path": path,
                "kind": "empty_array",
                "message": f"Array vazio. Considere adicionar '{path}_note' explicando.",
            })
        for i, item in enumerate(node):
            walk(item, item_schema, f"{path}[{i}]", findings)
        return


def validate_output(output_path: Path, schema: dict) -> list[dict]:
    with output_path.open(encoding="utf-8") as f:
        data = json.load(f)
    findings: list[dict] = []
    walk(data, schema, "", findings)
    return findings


def format_report(skill_id: str, findings: list[dict]) -> str:
    if not findings:
        return f"  ✓ {skill_id}: completo\n"

    by_sev = {"error": [], "warn": [], "info": []}
    for f in findings:
        by_sev[f["severity"]].append(f)

    lines = [f"  {skill_id}:"]
    for sev, icon in (("error", "✗"), ("warn", "⚠"), ("info", "·")):
        for f in by_sev[sev]:
            lines.append(f"    {icon} [{f['kind']}] {f['path']}")
            lines.append(f"        {f['message']}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("client_dir", type=Path)
    ap.add_argument("--skill", type=str, default=None, help="Validar apenas uma skill específica")
    ap.add_argument("--strict", action="store_true", help="Exit != 0 se houver warnings/errors")
    args = ap.parse_args()

    outputs_dir = args.client_dir / "outputs"
    if not outputs_dir.is_dir():
        print(f"Sem diretório de outputs em {outputs_dir}", file=sys.stderr)
        return 0

    targets: list[Path]
    if args.skill:
        p = outputs_dir / f"{args.skill}.json"
        if not p.exists():
            print(f"Output não encontrado: {p}", file=sys.stderr)
            return 1
        targets = [p]
    else:
        targets = sorted(outputs_dir.glob("*.json"))

    print(f"Validando {len(targets)} output(s) em {args.client_dir.name}:\n")

    total_errors = 0
    total_warns = 0
    for out_path in targets:
        skill_id = out_path.stem
        schema = load_schema(skill_id)
        if schema is None:
            print(f"  ? {skill_id}: schema não encontrado (pulado)\n")
            continue
        findings = validate_output(out_path, schema)
        total_errors += sum(1 for f in findings if f["severity"] == "error")
        total_warns += sum(1 for f in findings if f["severity"] == "warn")
        print(format_report(skill_id, findings))

    print(f"Resumo: {total_errors} erro(s), {total_warns} warning(s)")

    if args.strict and (total_errors > 0 or total_warns > 0):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
