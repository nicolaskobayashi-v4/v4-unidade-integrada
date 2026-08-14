#!/usr/bin/env python3
import csv, re, statistics as st
from collections import Counter, defaultdict

import os
from _paths import CSV
rows = list(csv.DictReader(open(os.path.join(CSV, "clientes-consolidado.csv"), encoding="utf-8-sig")))
abc = [r for r in rows if r["na_curva_abc"] == "1"]
for r in abc:
    r["total"] = float(r["total"]); r["qtde"] = int(r["qtde"]); r["tm"] = float(r["ticket_medio"])
    r["nm"] = int(r["n_marcas"]); r["nv"] = int(r["n_vendedores"])

TOT = sum(r["total"] for r in abc)
N = len(abc)
print(f"### BASE: {N} clientes com valor | R$ {TOT:,.2f} | {sum(r['qtde'] for r in abc)} unidades\n")

# ---------- A. Curva ABC por faturamento
print("=== A. CONCENTRAÇÃO DE FATURAMENTO ===")
srt = sorted(abc, key=lambda r: -r["total"])
acc, faixa, cortes = 0, {}, {}
for i, r in enumerate(srt, 1):
    acc += r["total"]
    p = acc / TOT
    if "A" not in cortes and p >= 0.80: cortes["A"] = (i, r["total"], p)
    if "B" not in cortes and p >= 0.95: cortes["B"] = (i, r["total"], p)
for k, (i, v, p) in cortes.items():
    print(f"  {p:.0%} da receita vem dos primeiros {i:,} clientes ({i/N:.1%}) — corte em R$ {v:,.2f}")
for pct in (0.01, 0.05, 0.10, 0.20, 0.50):
    k = int(N * pct)
    s = sum(r["total"] for r in srt[:k])
    print(f"  top {pct:>5.0%} ({k:>6,} clientes) = R$ {s:>14,.2f}  ({s/TOT:>5.1%} da receita)")
nA = cortes["A"][0]; nB = cortes["B"][0] - nA; nC = N - cortes["B"][0]
print(f"  → A={nA:,} ({nA/N:.1%})  B={nB:,} ({nB/N:.1%})  C={nC:,} ({nC/N:.1%})")
for nome, sub in (("A", srt[:nA]), ("B", srt[nA:nA+nB]), ("C", srt[nA+nB:])):
    s = sum(r["total"] for r in sub)
    print(f"     {nome}: R$ {s:>13,.2f} | ticket médio R$ {st.mean(r['tm'] for r in sub):>8,.2f} "
          f"| qtde média {st.mean(r['qtde'] for r in sub):>5.2f} | gasto médio R$ {s/len(sub):>9,.2f}")

# ---------- B. Ticket médio
print("\n=== B. TICKET MÉDIO (por cliente) ===")
tms = sorted(r["tm"] for r in abc)
print(f"  média R$ {st.mean(tms):,.2f} | mediana R$ {st.median(tms):,.2f} | "
      f"média ponderada (rec/qtde) R$ {TOT/sum(r['qtde'] for r in abc):,.2f}")
for q in (10, 25, 50, 75, 90, 95, 99):
    print(f"  P{q:<3} R$ {tms[int(len(tms)*q/100)-1]:>10,.2f}")
faixas = [(0,100),(100,200),(200,300),(300,400),(400,500),(500,750),(750,1000),(1000,1500),(1500,3000),(3000,10**9)]
print("  distribuição:")
for a, b in faixas:
    sel = [r for r in abc if a <= r["tm"] < b]
    if sel:
        s = sum(r["total"] for r in sel)
        rot = f"R$ {a:,}–{b:,}" if b < 10**9 else f"R$ {a:,}+"
        print(f"    {rot:<16} {len(sel):>6,} cli ({len(sel)/N:>5.1%})  R$ {s:>13,.2f} ({s/TOT:>5.1%} rec)")

# ---------- C. Recorrência
print("\n=== C. COMPRA ÚNICA vs RECORRENTE (qtde = unidades do relatório) ===")
grupos = [("1", lambda q: q == 1), ("2", lambda q: q == 2), ("3-5", lambda q: 3 <= q <= 5),
          ("6-10", lambda q: 6 <= q <= 10), ("11+", lambda q: q >= 11)]
for rot, f in grupos:
    sel = [r for r in abc if f(r["qtde"])]
    s = sum(r["total"] for r in sel)
    print(f"  qtde {rot:<5} {len(sel):>6,} cli ({len(sel)/N:>5.1%})  R$ {s:>13,.2f} ({s/TOT:>5.1%} rec)"
          f"  gasto médio R$ {s/len(sel):>9,.2f}  ticket médio R$ {st.mean(r['tm'] for r in sel):>8,.2f}")
u = [r for r in abc if r["qtde"] == 1]
print(f"  → {len(u)/N:.1%} da base tem qtde=1 e responde por {sum(r['total'] for r in u)/TOT:.1%} da receita")

# ---------- D. Geografia
print("\n=== D. GEOGRAFIA ===")
def norm_cidade(c):
    """O ERP trunca a cidade em ~20 caracteres, então agrupamos por truncamento.
    Caxias é inequívoca; os demais truncamentos ficam marcados com (?) porque
    'BENTO'/'PORTO'/'NOVA'/'SANTA' podem ser mais de um município."""
    c = re.sub(r"[^A-Z ]", " ", c.upper()); c = re.sub(r"\s+", " ", c).strip()
    if c in ("CAXIAS DO", "CAXIAS DO SUL", "CAXIAS", "CX DO SUL", "CAXIUAS DO", "CX SUL", "CAXIAS DO SU"):
        return "CAXIAS DO SUL"
    m = {"FLORES DA": "FLORES DA CUNHA", "BENTO": "BENTO GONCALVES (?)", "PORTO": "PORTO ALEGRE (?)",
         "NOVA": "NOVA ??? (truncado)", "ANTONIO": "ANTONIO PRADO (?)", "CARLOS": "CARLOS BARBOSA (?)",
         "CAMBARA DO": "CAMBARA DO SUL", "SAO FRANCISCO": "SAO FRANCISCO DE PAULA",
         "SANTA": "SANTA ??? (truncado)"}
    return m.get(c, c) or "(vazio)"
geo = defaultdict(lambda: [0, 0.0])
for r in abc:
    g = geo[norm_cidade(r["cidade"])]; g[0] += 1; g[1] += r["total"]
top = sorted(geo.items(), key=lambda x: -x[1][1])[:15]
for c, (n, v) in top:
    print(f"  {c:<26} {n:>6,} cli ({n/N:>5.1%})  R$ {v:>13,.2f} ({v/TOT:>5.1%})  gasto médio R$ {v/n:>8,.2f}")
cx = geo["CAXIAS DO SUL"]
print(f"  → Caxias do Sul = {cx[0]/N:.1%} dos clientes e {cx[1]/TOT:.1%} da receita")
fora = sum(v for c, (n, v) in geo.items() if c != "CAXIAS DO SUL")
print(f"  → fora de Caxias = R$ {fora:,.2f} ({fora/TOT:.1%})")

# ---------- E. Marcas
print("\n=== E. MARCAS ===")
MARCAS = ["ALTENBURG","NIAZITEX","BUDDEMEYER","KACYUMARA","KARSTEN","BELLA JANELA","TRUSSARDI","BUDD LUXUS","PLUMASSUL"]
col = {m: "m_" + m.lower().replace(" ", "_") for m in MARCAS}
print("  (valor = soma do gasto TOTAL do cliente, não faturamento da marca — indicador de afinidade)")
dados = []
for m in MARCAS:
    sel = [r for r in abc if r[col[m]] == "1"]
    if not sel: continue
    s = sum(r["total"] for r in sel)
    dados.append((m, len(sel), s, s/len(sel), st.mean(r["tm"] for r in sel), st.median(r["tm"] for r in sel)))
for m, n, s, gm, tmm, tmd in sorted(dados, key=lambda x: -x[3]):
    print(f"  {m:<13} {n:>6,} cli  gasto médio R$ {gm:>9,.2f}  ticket médio R$ {tmm:>8,.2f} (mediana {tmd:>8,.2f})")
semm = [r for r in abc if r["nm"] == 0]
print(f"  sem nenhuma das 9: {len(semm):,} cli ({len(semm)/N:.1%})  gasto médio R$ {sum(r['total'] for r in semm)/len(semm):,.2f}")
print("\n  nº de marcas por cliente:")
for k in range(0, 10):
    sel = [r for r in abc if r["nm"] == k]
    if not sel: continue
    s = sum(r["total"] for r in sel)
    print(f"    {k} marca(s): {len(sel):>6,} cli ({len(sel)/N:>5.1%})  gasto médio R$ {s/len(sel):>9,.2f}  "
          f"qtde média {st.mean(r['qtde'] for r in sel):>5.2f}  R$ {s:>12,.2f} ({s/TOT:>5.1%} rec)")

print("\n  cross-sell — clientes de cada marca que NÃO compraram as outras:")
for m in ["ALTENBURG", "KARSTEN", "TRUSSARDI"]:
    base = [r for r in abc if r[col[m]] == "1"]
    print(f"    quem compra {m} ({len(base):,} cli):")
    for o in MARCAS:
        if o == m: continue
        nao = [r for r in base if r[col[o]] == "0"]
        print(f"       nunca comprou {o:<13} {len(nao):>6,} ({len(nao)/len(base):>5.1%})")

# ---------- F. Base contatável
print("\n=== F. BASE CONTATÁVEL ===")
allr = rows
wa = [r for r in allr if r["whatsapp"]]
expl = [r for r in wa if r["whatsapp_ddd_assumido"] == "0"]
print(f"  total no consolidado: {len(allr):,}")
print(f"  com celular normalizado: {len(wa):,} ({len(wa)/len(allr):.1%}) | DDD explícito: {len(expl):,} ({len(expl)/len(allr):.1%})")
dup = Counter(r["whatsapp"] for r in wa)
print(f"  números repetidos (mesmo celular em >1 cadastro): {sum(v-1 for v in dup.values() if v>1):,} cadastros excedentes")
print("  cobertura por faixa ABC:")
setA = {r["codigo"] for r in srt[:nA]}; setB = {r["codigo"] for r in srt[nA:nA+nB]}
for nome, s in (("A", setA), ("B", setB)):
    sel = [r for r in allr if r["codigo"] in s]
    cw = sum(1 for r in sel if r["whatsapp"]); ce = sum(1 for r in sel if r["whatsapp"] and r["whatsapp_ddd_assumido"]=="0")
    print(f"    faixa {nome}: {len(sel):>6,} cli | com celular {cw:>6,} ({cw/len(sel):>5.1%}) | DDD explícito {ce:>6,} ({ce/len(sel):>5.1%})")
print(f"  com e-mail: {sum(1 for r in allr if r['email']):,} ({sum(1 for r in allr if r['email'])/len(allr):.2%})")

# ---------- G. Vendedores
print("\n=== G. VENDEDORES ===")
print(f"  clientes com 1 vendedor: {sum(1 for r in abc if r['nv']==1):,} | 2+: {sum(1 for r in abc if r['nv']>=2):,} "
      f"| 0 (sem vendedor): {sum(1 for r in abc if r['nv']==0):,}")
mult = [r for r in abc if r["nv"] >= 2]
print(f"  → {len(mult)/N:.1%} dos clientes foram atendidos por 2+ vendedores; gasto médio deles "
      f"R$ {sum(r['total'] for r in mult)/len(mult):,.2f} vs R$ "
      f"{sum(r['total'] for r in abc if r['nv']==1)/max(1,sum(1 for r in abc if r['nv']==1)):,.2f} de quem tem 1 só")
exc = defaultdict(lambda: [0, 0.0])
for r in abc:
    if r["nv"] == 1:
        v = r["vendedores"]; exc[v][0] += 1; exc[v][1] += r["total"]
print("  carteira exclusiva (clientes atendidos SÓ por aquele vendedor) — top 12 por receita:")
for v, (n, s) in sorted(exc.items(), key=lambda x: -x[1][1])[:12]:
    print(f"    {v:<38} {n:>5,} cli  R$ {s:>12,.2f}  gasto médio R$ {s/n:>8,.2f}")
