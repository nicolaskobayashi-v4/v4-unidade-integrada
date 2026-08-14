#!/usr/bin/env python3
"""Une os 4 CSVs em uma tabela única de cliente (1 linha = 1 cliente)."""
import csv, os, re
from collections import defaultdict

from _paths import CSV

MARCAS = ["ALTENBURG", "NIAZITEX", "BUDDEMEYER", "KACYUMARA", "KARSTEN",
          "BELLA JANELA", "TRUSSARDI", "BUDD LUXUS", "PLUMASSUL"]
DDD_PADRAO = "54"  # Caxias do Sul — base é majoritariamente local


def ler(nome):
    with open(os.path.join(CSV, nome), encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def normaliza_fone(bruto):
    """-> (numero_e164_sem_+, tipo, ddd_assumido) ou (None, motivo, False)."""
    d = re.sub(r"\D", "", bruto or "")
    if not d:
        return None, "vazio", False
    d = d.lstrip("0")
    if d.startswith("55") and len(d) in (12, 13):
        d = d[2:]
    if len(d) == 11 and d[2] == "9":
        return "55" + d, "celular", False
    if len(d) == 10 and d[2] in "89":
        return "55" + d[:2] + "9" + d[2:], "celular_8dig", False
    if len(d) == 10 and d[2] in "2345":
        return "55" + d, "fixo", False
    if len(d) == 9 and d[0] == "9":
        return "55" + DDD_PADRAO + d, "celular", True
    if len(d) == 8 and d[0] in "89":
        return "55" + DDD_PADRAO + "9" + d, "celular_8dig", True
    if len(d) == 8 and d[0] in "2345":
        return "55" + DDD_PADRAO + d, "fixo", True
    return None, "invalido", False


def melhor_whatsapp(fones):
    """Prefere celular completo com DDD real; depois 8 dígitos; depois DDD assumido."""
    cands = []
    for f in fones:
        num, tipo, assumido = normaliza_fone(f)
        if num and tipo.startswith("celular"):
            prio = (0 if not assumido else 1, 0 if tipo == "celular" else 1)
            cands.append((prio, num, assumido))
    if not cands:
        return "", False
    cands.sort()
    return cands[0][1], cands[0][2]


abc = {int(r["codigo"]): r for r in ler("curva-abc-clientes.csv")}
emails = {int(r["codigo"]): r for r in ler("clientes-email-telefones.csv")}

vend = defaultdict(set)
fones_extra = defaultdict(set)
nomes = {}
for r in ler("clientes-por-vendedor.csv"):
    c = int(r["codigo"])
    if r["vendedor_id"]:
        vend[c].add((int(r["vendedor_id"]), r["vendedor_nome"]))
    for k in ("telefone", "celular", "fone_emprego"):
        if r[k]:
            fones_extra[c].add(r[k])
    nomes.setdefault(c, r["nome"])

marcas = defaultdict(set)
for r in ler("clientes-por-marca.csv"):
    c = int(r["codigo"])
    marcas[c].add(r["marca"])
    if r["vendedor_id"]:
        vend[c].add((int(r["vendedor_id"]), r["vendedor_nome"]))
    nomes.setdefault(c, r["nome"])

for c, r in emails.items():
    if r["vendedor_id"]:
        vend[c].add((int(r["vendedor_id"]), r["vendedor_nome"]))
    nomes.setdefault(c, r["nome"])

todos = sorted(set(abc) | set(emails) | set(vend) | set(marcas))

cab = (["codigo", "nome", "cidade", "uf", "na_curva_abc", "qtde", "total", "ticket_medio",
        "rank_qtde", "email", "whatsapp", "whatsapp_ddd_assumido", "telefones_brutos",
        "n_vendedores", "vendedores", "n_marcas", "marcas"]
       + ["m_" + m.lower().replace(" ", "_") for m in MARCAS])

linhas = []
for c in todos:
    a = abc.get(c)
    e = emails.get(c)
    fones = set()
    for src, keys in ((a, ("telefone1", "telefone2", "celular")),
                      (e, ("telefone", "fax", "celular"))):
        if src:
            fones |= {src[k] for k in keys if src[k]}
    fones |= fones_extra.get(c, set())
    wa, assumido = melhor_whatsapp(fones)
    vs = sorted(vend.get(c, ()))
    ms = sorted(marcas.get(c, ()))
    nome = (a or e or {}).get("nome") or nomes.get(c, "")
    linhas.append([
        c, nome,
        a["cidade"] if a else "", a["uf"] if a else "",
        1 if a else 0,
        a["qtde"] if a else "", a["total"] if a else "", a["ticket_medio"] if a else "",
        a["rank_qtde"] if a else "",
        e["email"] if e else "",
        wa, 1 if assumido else 0,
        " | ".join(sorted(fones)),
        len(vs), " | ".join(f"{i}-{n}" for i, n in vs),
        len(ms), " | ".join(ms),
    ] + [1 if m in marcas.get(c, ()) else 0 for m in MARCAS])

with open(os.path.join(CSV, "clientes-consolidado.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(cab)
    w.writerows(linhas)

# ---- tabela de vendedores (o rodapé do PDF é acumulado e não serve)
cont = defaultdict(lambda: [0, 0, 0.0])
for c in todos:
    for i, n in vend.get(c, ()):
        cont[(i, n)][0] += 1
        if c in abc:
            cont[(i, n)][1] += 1
            cont[(i, n)][2] += float(abc[c]["total"])
with open(os.path.join(CSV, "vendedores.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["vendedor_id", "vendedor_nome", "clientes_na_carteira",
                "clientes_com_valor_na_abc", "soma_total_clientes_abc"])
    for (i, n), (t, cv, sv) in sorted(cont.items(), key=lambda x: -x[1][0]):
        w.writerow([i, n, t, cv, round(sv, 2)])

# ---- validação
n_abc = sum(r[4] for r in linhas)
soma = sum(float(r[6]) for r in linhas if r[6] != "")
qt = sum(int(r[5]) for r in linhas if r[5] != "")
com_wa = sum(1 for r in linhas if r[10])
wa_assum = sum(1 for r in linhas if r[11])
wa_unicos = len({r[10] for r in linhas if r[10]})
com_email = sum(1 for r in linhas if r[9])
print(f"clientes no consolidado : {len(linhas)}")
print(f"  na Curva ABC (c/ valor): {n_abc}  (esperado 31891)")
print(f"  fora da ABC (s/ valor) : {len(linhas)-n_abc}")
print(f"  soma total             : {soma:,.2f}  (esperado 28,810,734.33)")
print(f"  soma qtde              : {qt}  (esperado 54366)")
print(f"  com e-mail             : {com_email}")
print(f"  com whatsapp normalizado: {com_wa} ({com_wa/len(linhas):.1%})  únicos: {wa_unicos}  com DDD assumido: {wa_assum}")
print(f"  vendedores mapeados    : {len(cont)}")
