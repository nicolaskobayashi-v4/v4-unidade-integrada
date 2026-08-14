#!/usr/bin/env python3
"""Parser da Curva ABC (CX0077T) -> CSV.

Estratégia: pdftotext -layout preserva colunas com posição de caractere consistente
DENTRO de cada página (mas variável ENTRE páginas). Então lemos página a página,
achamos o cabeçalho e usamos os offsets dele para fatiar as linhas.
As 3 colunas numéricas finais (Qtde/Total/T.Médio) são extraídas por regex na cauda,
que é inequívoca (int, decimal-vírgula, decimal-vírgula).
"""
import csv, os, re, sys, unicodedata
from _paths import TXT as TXTDIR, CSV, garante_txt

garante_txt()
TXT = os.path.join(TXTDIR, "Curva ABC de Clientes por Quantidade com Ticket Médio.txt")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(CSV, "curva-abc-clientes.csv")

TAIL = re.compile(r"\s+(\d[\d.]*)\s+(-?[\d.]+,\d{2})\s+(-?[\d.]+,\d{2})\s*$")

UFS = {"RS","SC","PR","SP","RJ","MG","ES","BA","GO","DF","MT","MS","PE","CE","PA","AM","PB","RN","AL","SE","PI","MA","TO","RO","AC","AP","RR"}


def num(s):
    return float(s.replace(".", "").replace(",", "."))


def limpa(s):
    return re.sub(r"\s+", " ", s).strip()


def split_cidade(raw):
    """'Caxias do Sul/RS' -> ('CAXIAS DO SUL','RS'); 'CAXIAS DO' -> ('CAXIAS DO','')."""
    r = limpa(raw)
    uf = ""
    if "/" in r:
        cid, _, tail = r.rpartition("/")
        tail = tail.strip().upper()
        if tail in UFS:
            uf = tail
            r = cid.strip()
        elif tail == "":
            r = cid.strip()
    cid = unicodedata.normalize("NFKD", r.upper())
    cid = "".join(c for c in cid if not unicodedata.combining(c))
    return limpa(cid), uf


def main():
    paginas = open(TXT, encoding="utf-8").read().split("\f")
    linhas, descartes, paginas_sem_header = [], [], 0

    for pag in paginas:
        ls = pag.split("\n")
        hdr = next((l for l in ls if "Rank" in l and "Código" in l and "T.Médio" in l), None)
        if hdr is None:
            if any(re.match(r"^\s*\d+\s+\d+\s+\S", l) for l in ls):
                paginas_sem_header += 1
            continue
        o = {k: hdr.find(k) for k in ("Rank", "Código", "Nome", "Cidade/UF", "Telefone 1", "Telefone 2", "Celular", "Qtde")}
        i = ls.index(hdr)
        for l in ls[i + 1:]:
            if not l.strip():
                continue
            if "Total Geral" in l:
                continue
            m = TAIL.search(l)
            if not m:
                if re.match(r"^\s*\d+\s+\d+\s+\S", l):
                    descartes.append(l)
                continue
            corpo = l[: m.start()]
            rank = corpo[o["Rank"]:o["Código"]].strip()
            cod = corpo[o["Código"]:o["Nome"]].strip()
            if not (rank.isdigit() and cod.isdigit()):
                descartes.append(l)
                continue
            nome = limpa(corpo[o["Nome"]:o["Cidade/UF"]])
            cid_raw = limpa(corpo[o["Cidade/UF"]:o["Telefone 1"]])
            tel1 = limpa(corpo[o["Telefone 1"]:o["Telefone 2"]])
            tel2 = limpa(corpo[o["Telefone 2"]:o["Celular"]])
            cel = limpa(corpo[o["Celular"]:])
            cid, uf = split_cidade(cid_raw)
            linhas.append([int(rank), int(cod), nome, cid_raw, cid, uf, tel1, tel2, cel,
                           int(m.group(1).replace(".", "")), num(m.group(2)), num(m.group(3))])

    with open(OUT, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["rank_qtde", "codigo", "nome", "cidade_raw", "cidade", "uf",
                    "telefone1", "telefone2", "celular", "qtde", "total", "ticket_medio"])
        w.writerows(linhas)

    q = sum(r[9] for r in linhas)
    t = sum(r[10] for r in linhas)
    print(f"linhas={len(linhas)}  qtde={q}  total={t:,.2f}")
    print(f"esperado (rodapé do PDF): linhas=31891  qtde=54366  total=28,810,734.33")
    print(f"páginas sem header={paginas_sem_header}  descartes={len(descartes)}")
    for d in descartes[:10]:
        print("  DESCARTE:", repr(d))


main()
