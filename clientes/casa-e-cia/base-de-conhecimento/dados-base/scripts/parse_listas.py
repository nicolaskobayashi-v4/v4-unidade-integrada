#!/usr/bin/env python3
"""Parser dos relatórios de lista de clientes (CX0043C e CL1002V) -> CSV.

Ambos são listas agrupadas por vendedor, sem valores. Diferem só nas colunas de contato.
Cada chunk (bloco separado por 2+ espaços) é atribuído à coluna cujo intervalo
tem maior sobreposição — isso tolera as variações de largura que o pdftotext
introduz em páginas com poucas linhas.
"""
import csv, os, re, sys
from _paths import TXT, CSV, garante_txt

garante_txt()

RUIDO = re.compile(
    r"Ordem:|Data de:|Filial de:|Cliente de:|Grupo de:|Versão|Quantidade de |"
    r"Relacao de Clientes|Clientes com Compras|CASA E CIA|^ANDERSON MOREIRA")
VEND = re.compile(r"Vendedor:\s*(\d*)\s*-\s*(.*?)\s*$")


def limpa(s):
    return re.sub(r"\s+", " ", s).strip()


def chunks(linha):
    """[(inicio, texto)] separando por 2+ espaços."""
    return [(m.start(), m.group().strip()) for m in re.finditer(r"\S(?:.*?\S)?(?=\s{2,}|$)", linha) if m.group().strip()]


def parse(arquivo, colunas, hdr_marca):
    """colunas: lista de rótulos do cabeçalho, na ordem. Retorna (linhas, n_vendedores)."""
    paginas = open(os.path.join(TXT, arquivo), encoding="utf-8").read().split("\f")
    out, vend_id, vend_nome, vistos_vend = [], "", "", set()
    sem_header = 0

    for pag in paginas:
        ls = pag.split("\n")
        hdr = next((l for l in ls if all(c in l for c in hdr_marca)), None)
        if hdr is None:
            hdr_off = None
        else:
            hdr_off = [hdr.find(c) for c in colunas]
            # limite direito de cada coluna
            spans = [(hdr_off[i], hdr_off[i + 1] if i + 1 < len(hdr_off) else 10**6)
                     for i in range(len(hdr_off))]
        for l in ls:
            if not l.strip() or RUIDO.search(l):
                mv = VEND.search(l) if "Vendedor:" in l and "Ordem:" not in l else None
                if mv:
                    vend_id, vend_nome = mv.group(1) or "0", limpa(mv.group(2))
                    vistos_vend.add((vend_id, vend_nome))
                continue
            if "Vendedor:" in l:
                mv = VEND.search(l)
                if mv:
                    vend_id, vend_nome = mv.group(1) or "0", limpa(mv.group(2))
                    vistos_vend.add((vend_id, vend_nome))
                continue
            if hdr is not None and l is hdr:
                continue
            ch = chunks(l)
            if not ch:
                continue
            m = re.match(r"^(\d{1,8})(?:\s+(.*))?$", ch[0][1])
            if not m:
                continue
            if hdr_off is None:
                sem_header += 1
                continue
            cod, resto = m.group(1), (m.group(2) or "")
            campos = [""] * len(colunas)
            campos[1] = resto  # nome pode vir colado ao código
            for ini, txt in ch[1:]:
                if "@" in txt and "E-Mail" in colunas:
                    j = colunas.index("E-Mail")
                    campos[j] = (campos[j] + " " + txt).strip()
                    continue
                fim = ini + len(txt)
                melhor, mscore = None, 0
                for j in range(1, len(colunas)):
                    a, b = spans[j]
                    ov = min(fim, b) - max(ini, a)
                    if ov > mscore:
                        melhor, mscore = j, ov
                if melhor is None:
                    melhor = min(range(1, len(colunas)), key=lambda j: abs(spans[j][0] - ini))
                campos[melhor] = (campos[melhor] + " " + txt).strip()
            campos[0] = cod
            out.append([int(cod)] + [limpa(c) for c in campos[1:]] + [vend_id, vend_nome])

    return out, sorted(vistos_vend, key=lambda x: int(x[0])), sem_header


def grava(caminho, cabecalho, linhas):
    with open(caminho, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(cabecalho)
        w.writerows(linhas)


if __name__ == "__main__":

    # ---- 1. E-mails e telefones (CX0043C) — esperado 31.729
    cols = ["Código", "Nome do Cliente", "Telefone", "Fax", "Celular", "E-Mail"]
    l, v, sh = parse("Clientes com Compras no Periodo com Email eTelefones.txt", cols,
                     ("Código", "Nome do Cliente", "E-Mail"))
    grava(os.path.join(CSV, "clientes-email-telefones.csv"),
          ["codigo", "nome", "telefone", "fax", "celular", "email", "vendedor_id", "vendedor_nome"], l)
    ncom = sum(1 for r in l if "@" in r[5])
    print(f"[emails]  linhas={len(l)} (esperado 31729)  únicos={len({r[0] for r in l})}  "
          f"vendedores={len(v)}  com e-mail={ncom}  sem_header={sh}")

    # ---- 2. Geral por piso (CL1002V) — esperado 42.595
    cols = ["Código", "Nome do Cliente", "Telefone", "Celular", "Fone Emprego"]
    l, v, sh = parse("Relacao de Clientes com Compras no Periodo por Grupo por Vendedor.txt", cols,
                     ("Código", "Nome do Cliente", "Fone Emprego"))
    grava(os.path.join(CSV, "clientes-por-vendedor.csv"),
          ["codigo", "nome", "telefone", "celular", "fone_emprego", "vendedor_id", "vendedor_nome"], l)
    print(f"[geral]   linhas={len(l)} (esperado 42595)  únicos={len({r[0] for r in l})}  "
          f"vendedores={len(v)}  sem_header={sh}")

    # ---- 3. Nove relatórios por marca
    MARCAS = {
        "ALTENBURG": ("Relacao de Clientes com Compras no Periodo por Grupo por Vendedor ALTENBURG.txt", 12990),
        "NIAZITEX": ("Relacao de Clientes com Compras no Periodo por Grupo por Vendedor NIAZITEX.txt", 6719),
        "BUDDEMEYER": ("Relacao de Clientes com Compras no Periodo por Grupo por Vendedor BUDDEMETER.txt", 6343),
        "KACYUMARA": ("Relacao de Clientes com Compras no Periodo por Grupo por Vendedor KACYUMARA.txt", 5495),
        "KARSTEN": ("Relacao de Clientes com Compras no Periodo por Grupo por Vendedor  KARSTEN.txt", 5270),
        "BELLA JANELA": ("Relacao de Clientes com Compras no Periodo por Grupo por Vendedor BELLA JANELA.txt", 5084),
        "TRUSSARDI": ("Relacao de Clientes com Compras no Periodo por Grupo por Vendedor    TRUSSARDI.txt", 2640),
        "BUDD LUXUS": ("Relacao de Clientes com Compras no Periodo por Grupo por Vendedor  LUXUS.txt", 1495),
        "PLUMASSUL": ("Relacao de Clientes com Compras no Periodo por Grupo por Vendedor  PLUMASSUL.txt", 279),
    }
    MARCAS["PLUMASSUL"] = ("Relacao de Clientes com Compras no Periodo por Grupo por Vendedor  PLUMASUL.txt", 279)
    todas = []
    for marca, (arq, esperado) in MARCAS.items():
        l, v, sh = parse(arq, cols, ("Código", "Nome do Cliente", "Fone Emprego"))
        ok = "OK " if len(l) == esperado else "!! "
        print(f"[{ok}{marca:<13}] linhas={len(l):>6} (esperado {esperado:>6})  únicos={len({r[0] for r in l}):>6}  sem_header={sh}")
        for r in l:
            todas.append([r[0], r[1], marca, r[5], r[6]])
    grava(os.path.join(CSV, "clientes-por-marca.csv"),
          ["codigo", "nome", "marca", "vendedor_id", "vendedor_nome"], todas)
    print(f"[marcas]  total={len(todas)} (esperado 46315)  clientes únicos={len({r[0] for r in todas})}")
