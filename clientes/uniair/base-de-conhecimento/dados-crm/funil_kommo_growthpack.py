#!/usr/bin/env python3
"""Funil Uniair: GrowthPack (formulário pago) x Kommo, janela 02/06 a 06/08/2026."""
import csv, re, collections, datetime, statistics

BC = "/Users/lucascalefigoncalves/Documents/Code/EE3/estruturacao-ia/clientes/uniair/base-de-conhecimento"
INI, FIM = datetime.date(2026, 6, 2), datetime.date(2026, 8, 3)

DESCARTE = {"Passagem Aérea", "Trabalhar na Uniair / Enviar Currículo"}

CAMP = {
    "v4searchaeromedicos": "Aeromédico PR/RS/SC/SP",
    "v4searchaeromedicosdemaisestados": "Aeromédico Demais Estados",
    "v4searchaeromedicossaopaulo": "Aeromédico SP",
    "v4searchtaxiaereooutros": "Táxi aéreo SC/RS/PR",
    "v4searchtaxiaereosaopaulo": "Táxi aéreo SP",
    "v4searchtaxiaereospprsp": "Táxi aéreo SC/RS/PR",
    "v4searchinstitucional": "Institucional/Marca",
    "v4searchaeromedicosrgsul": "Aeromédico Demais Estados",
    "v4searchaeromedicosparana": "Aeromédico PR/RS/SC/SP",
    "v4aromedicoamerica": "Aeromédico América S",
    "v5searchaeromedicos_escala": "Aeromédico PR/RS/SC/SP",
}
GADS = {
    "v4 |🧑‍⚕️| search_aeromedico_s | PR, RS, SC e SP": "Aeromédico PR/RS/SC/SP",
    "v4 |🧑‍⚕️| search_aeromedico_s | Demais Estados": "Aeromédico Demais Estados",
    "v4 |🧑‍⚕️| search_aeromedico_s | SP": "Aeromédico SP",
    "v4 |✈️| search_taxiaereo_outros | SC, RS e PR": "Táxi aéreo SC/RS/PR",
    "v4 |✈️| search_taxiaereo | SP": "Táxi aéreo SP",
    "v4 | search_institucional | BR": "Institucional/Marca",
    "v4 |🧑‍⚕️| aeromedico | América S": "Aeromédico América S",
}
ORDEM = ["Aeromédico PR/RS/SC/SP", "Aeromédico Demais Estados", "Aeromédico SP",
         "Táxi aéreo SC/RS/PR", "Táxi aéreo SP", "Institucional/Marca",
         "Aeromédico América S", "Outras/sem UTM"]

def fone(t):
    d = re.sub(r"\D", "", t or "")
    return d[-8:] if len(d) >= 8 else None
def num(s):
    try: return float((s or "0").replace(".", "").replace(",", "."))
    except ValueError: return 0.0
def dtgp(s):
    try: return datetime.datetime.strptime(s[:19], "%Y-%m-%d %H:%M:%S")
    except ValueError: return None

# ---- GrowthPack ----
gp = list(csv.DictReader(open(f"{BC}/dados-crm/GrowthPack _ Uniair - Base de Leads (4).csv", encoding="utf-8-sig")))
for r in gp:
    r["_dt"] = dtgp(r["Data da Conversão"])
    r["_camp"] = CAMP.get((r["UTM_Campaign"] or "").strip(), "Outras/sem UTM")
    r["_mot"] = r["Qual_o_motivo_do_seu_contato"] or "(vazio)"
    r["_mql"] = r["_mot"] not in DESCARTE and r["_mot"] != "(vazio)"
gpj = [r for r in gp if r["_dt"] and INI <= r["_dt"].date() <= FIM]

# ---- Kommo ----
km = list(csv.DictReader(open(f"{BC}/dados-de-midia/leads_kommo.csv", encoding="utf-8-sig"), delimiter=";"))
for r in km:
    r["_dt"] = datetime.datetime.strptime(r["Data Criada"], "%d/%m/%Y %H:%M")
kmj = [r for r in km if INI <= r["_dt"].date() <= FIM]
kset = set(f for f in (fone(r["Telefone"]) for r in km) if f)

idx = collections.defaultdict(list)
for r in gpj:
    k = fone(r["telefone_Whatsapp"])
    if k: idx[k].append(r)
for k in idx: idx[k].sort(key=lambda r: r["_dt"])

def valor(r): return num(r["Valor (Venda)"])
def teve_orc(r): return valor(r) > 0 or bool(r["Aeronave"].strip())
def est(r):
    e = r["Etapa do Lead"]
    if e == "Fechado - ganho": return 5
    if e == "Discussão de contrato": return 4
    if e == "ORÇAMENTO ENVIADO": return 3
    if e == "Contato inicial": return 2 if (teve_orc(r) or r["Finalidade"].strip()) else 1
    if e == "Leads de entrada": return 0
    if e == "Fechado - perdido":
        if teve_orc(r): return 3
        return 1 if r["Motivo da Perda"].strip() else 0
    return 0
for r in kmj:
    k = fone(r["Telefone"])
    g = idx[k][0] if k and k in idx else None
    r["_gp"] = g
    r["_camp"] = g["_camp"] if g else "Não rastreado"
    r["_st"] = est(r)

# ---- investimento ----
def load_std(f):
    return list(csv.DictReader(open(f"{BC}/dados-de-midia/{f}", encoding="utf-8-sig").read().split("\n")[2:]))
inv = collections.defaultdict(lambda: collections.defaultdict(float))
seen = set()
for f in ["STD Report 1-6 a 2-8.csv", "STD Report-260701-260805.csv", "STD Report (12).csv"]:
    for r in load_std(f):
        d = r.get("Dia") or ""
        if not ("2026-06-02" <= d <= "2026-08-03"): continue
        k = (d, r["Campanha"], r["Grupo de anúncios"])
        if k in seen: continue
        seen.add(k)
        c = GADS.get(r["Campanha"], "Outras/sem UTM")
        inv[c]["custo"] += num(r["Custo"]); inv[c]["conv"] += num(r["Conversões"])
        inv[c]["cliques"] += num(r["Cliques"]); inv[c]["impr"] += num(r["Impr."])

TOT = sum(v["custo"] for v in inv.values())
print(f"### JANELA {INI:%d/%m} a {FIM:%d/%m/%Y} · investimento Google Ads R$ {TOT:,.2f}")
print(f"Formulários GrowthPack: {len(gpj)} | Leads no Kommo: {len(kmj)}")
print()

# ---- tabela mestre por campanha ----
print("=" * 132)
print(f"{'campanha':27s}{'invest':>10s}{'cliq':>7s}{'form':>6s}{'MQL':>6s}{'%MQL':>7s}{'noCRM':>7s}{'CI':>5s}{'Disc':>6s}{'Orç':>5s}{'Ctr':>5s}{'Gan':>5s}{'R$/form':>9s}{'R$/MQL':>9s}{'R$/CRM':>9s}{'R$/Orç':>9s}")
print("=" * 132)
tot = collections.Counter()
for c in ORDEM:
    f = [r for r in gpj if r["_camp"] == c]
    mql = [r for r in f if r["_mql"]]
    crm = [r for r in kmj if r["_camp"] == c]
    st = [sum(1 for r in crm if r["_st"] >= i) for i in range(6)]
    i_ = inv[c]["custo"]
    def d(x, n): return f"R$ {x/n:,.0f}" if n and x else "—"
    print(f"{c:27s}{i_:10,.0f}{inv[c]['cliques']:7,.0f}{len(f):6d}{len(mql):6d}{(len(mql)/len(f)*100 if f else 0):6.0f}%{len(crm):7d}{st[1]:5d}{st[2]:6d}{st[3]:5d}{st[4]:5d}{st[5]:5d}{d(i_,len(f)):>9s}{d(i_,len(mql)):>9s}{d(i_,len(crm)):>9s}{d(i_,st[3]):>9s}")
    tot["inv"] += i_; tot["cliq"] += inv[c]["cliques"]; tot["form"] += len(f); tot["mql"] += len(mql)
    tot["crm"] += len(crm)
    for i in range(6): tot[f"st{i}"] += st[i]
print("-" * 132)
print(f"{'TOTAL PAGO RASTREADO':27s}{tot['inv']:10,.0f}{tot['cliq']:7,.0f}{tot['form']:6d}{tot['mql']:6d}{tot['mql']/tot['form']*100:6.0f}%{tot['crm']:7d}{tot['st1']:5d}{tot['st2']:6d}{tot['st3']:5d}{tot['st4']:5d}{tot['st5']:5d}"
      f"{'R$ '+format(tot['inv']/tot['form'],',.0f'):>9s}{'R$ '+format(tot['inv']/tot['mql'],',.0f'):>9s}{'R$ '+format(tot['inv']/tot['crm'],',.0f'):>9s}{'R$ '+format(tot['inv']/tot['st3'],',.0f'):>9s}")
nr = [r for r in kmj if r["_camp"] == "Não rastreado"]
st = [sum(1 for r in nr if r["_st"] >= i) for i in range(6)]
print(f"{'NÃO RASTREADO (CRM)':27s}{'—':>10s}{'—':>7s}{'—':>6s}{'—':>6s}{'—':>7s}{len(nr):7d}{st[1]:5d}{st[2]:6d}{st[3]:5d}{st[4]:5d}{st[5]:5d}")
print()

# ---- conversão entre etapas ----
print("### FUNIL — TODOS OS LEADS DO CRM (n=%d)" % len(kmj))
st = [sum(1 for r in kmj if r["_st"] >= i) for i in range(6)]
nomes = ["Leads de entrada", "Contato inicial", "Discussões", "Orçamento enviado", "Discussão de contrato", "Fechado ganho"]
for i, n in enumerate(nomes):
    tx = f"{st[i]/st[i-1]*100:5.1f}%" if i else "     —"
    ac = f"{st[i]/st[0]*100:5.1f}%"
    print(f"  {n:24s}{st[i]:5d}   etapa n/n-1: {tx}   acum: {ac}")
print()
print("### FUNIL — SÓ MÍDIA PAGA RASTREADA (n=%d no CRM)" % tot["crm"])
for i, n in enumerate(nomes):
    v = tot[f"st{i}"]
    tx = f"{v/tot[f'st{i-1}']*100:5.1f}%" if i and tot[f"st{i-1}"] else "     —"
    print(f"  {n:24s}{v:5d}   etapa n/n-1: {tx}   custo/etapa: R$ {tot['inv']/v:,.2f}" if v else f"  {n:24s}{v:5d}")
print()
print("  [+ camada de mídia] formulários %d → MQL %d (%.0f%%) → chegou ao CRM %d (%.0f%% dos MQL)"
      % (tot["form"], tot["mql"], tot["mql"]/tot["form"]*100, tot["crm"], tot["crm"]/tot["mql"]*100))
print()

# ---- conversões Google Ads x formulários ----
print("### MENSURAÇÃO: conversões reportadas pelo Google Ads x formulários reais")
print(f"{'campanha':27s}{'conv GAds':>10s}{'form':>7s}{'MQL':>6s}{'conv/form':>11s}{'CPA GAds':>10s}{'CP MQL real':>13s}")
for c in ORDEM:
    f = [r for r in gpj if r["_camp"] == c]
    mql = [r for r in f if r["_mql"]]
    cv = inv[c]["conv"]; i_ = inv[c]["custo"]
    if not f and not cv: continue
    print(f"{c:27s}{cv:10.0f}{len(f):7d}{len(mql):6d}{(cv/len(f)*100 if f else 0):10.0f}%"
          f"{('R$ '+format(i_/cv,',.0f')) if cv else '—':>10s}{('R$ '+format(i_/len(mql),',.0f')) if mql else '—':>13s}")
print()

# ---- motivos de descarte por campanha ----
print("### O QUE O FORMULÁRIO ESTÁ CAPTURANDO (janela)")
mm = collections.defaultdict(collections.Counter)
for r in gpj: mm[r["_camp"]][r["_mot"]] += 1
for c in ORDEM:
    if not mm[c]: continue
    t = sum(mm[c].values())
    desc = sum(v for k, v in mm[c].items() if k in DESCARTE)
    print(f"  {c} — {t} formulários, {desc} de descarte ({desc/t*100:.0f}%)")
    for k, v in mm[c].most_common():
        flag = "  ✗" if k in DESCARTE else "   "
        print(f"     {v:4d} ({v/t*100:4.0f}%){flag} {k}")
print()
tt = collections.Counter(r["_mot"] for r in gpj)
d = sum(v for k, v in tt.items() if k in DESCARTE)
print(f"  TOTAL: {sum(tt.values())} formulários · {d} descarte ({d/sum(tt.values())*100:.0f}%) · custo do descarte ≈ R$ {TOT*d/sum(tt.values()):,.0f}")
print()

# ---- perdas ----
print("### MOTIVOS DE PERDA (CRM, janela)")
perd = [r for r in kmj if r["Etapa do Lead"] == "Fechado - perdido"]
for k, v in collections.Counter(r["Motivo da Perda"] or "(vazio)" for r in perd).most_common():
    orc = sum(1 for r in perd if (r["Motivo da Perda"] or "(vazio)") == k and teve_orc(r))
    print(f"  {v:4d} ({v/len(perd)*100:4.1f}%)  {k:30s} dos quais {orc} já tinham orçamento")
print(f"  total perdidos: {len(perd)} de {len(kmj)} ({len(perd)/len(kmj)*100:.0f}%)")
print()

# ---- receita / ticket / ciclo ----
gan = [r for r in kmj if r["Etapa do Lead"] == "Fechado - ganho"]
vs = [valor(r) for r in gan if valor(r) > 0]
print("### GANHOS")
print(f"  {len(gan)} ganhos · {len(vs)} com valor · receita R$ {sum(vs):,.2f} · ticket médio R$ {statistics.mean(vs):,.2f} · mediana R$ {statistics.median(vs):,.2f}")
print(f"  maior R$ {max(vs):,.2f} · menor R$ {min(vs):,.2f} · {len(gan)-len(vs)} ganhos SEM valor registrado")
print("  por campanha:")
for c in collections.Counter(r["_camp"] for r in gan):
    rr = [r for r in gan if r["_camp"] == c]
    print(f"     {c:27s} {len(rr):3d} ganhos · R$ {sum(valor(r) for r in rr):,.0f}")
cic = []
for r in gan:
    if r["Fechada em"].strip():
        try:
            fd = datetime.datetime.strptime(r["Fechada em"][:10], "%d/%m/%Y")
            cic.append((fd - r["_dt"]).days)
        except ValueError: pass
print(f"  ciclo dos ganhos: mediana {statistics.median(cic):.0f}d · média {statistics.mean(cic):.1f}d · máx {max(cic)}d")
print()

# ---- por mês ----
print("### POR MÊS (leads do CRM)")
for m in ["2026-06", "2026-07", "2026-08"]:
    rr = [r for r in kmj if r["_dt"].strftime("%Y-%m") == m]
    s = [sum(1 for r in rr if r["_st"] >= i) for i in range(6)]
    g = sum(valor(r) for r in rr if r["Etapa do Lead"] == "Fechado - ganho")
    gpm = [r for r in gpj if r["_dt"].strftime("%Y-%m") == m]
    mqlm = sum(1 for r in gpm if r["_mql"])
    inv_m = 0.0
    for f in ["STD Report 1-6 a 2-8.csv", "STD Report-260701-260805.csv", "STD Report (12).csv"]:
        pass
    print(f"  {m}: form={len(gpm):3d} MQL={mqlm:3d} | CRM leads={s[0]:3d} orç={s[3]:3d} contrato={s[4]:3d} ganhos={s[5]:3d} receita=R$ {g:,.0f}")
print()

# ---- responsáveis ----
print("### RESPONSÁVEL / VENDEDORA")
print(" Lead usuário responsável:", collections.Counter(r["Lead usuário responsável"] or "(vazio)" for r in kmj).most_common())
print(" Vendedora:", collections.Counter(r["Vendedora"] or "(vazio)" for r in kmj).most_common())
print(" Vendedora dos ganhos:", collections.Counter(r["Vendedora"] or "(vazio)" for r in gan).most_common())
