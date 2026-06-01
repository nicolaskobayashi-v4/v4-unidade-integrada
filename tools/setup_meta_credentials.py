#!/usr/bin/env python3
"""
Setup interativo de credenciais Meta Graph API.

Uso:
  python3 tools/setup_meta_credentials.py

Pede short token + app secret, troca por long-lived (60 dias),
salva em .credentials/meta-graph-api.json e testa com chamada à API.
"""
import json
import urllib.request
import urllib.parse
import urllib.error
import sys
from pathlib import Path

APP_ID = "1346202230719387"
CRED_PATH = Path(".credentials/meta-graph-api.json")
# Username público de Instagram usado só para validar o token (troque se quiser).
TEST_TARGET = "instagram"


def main():
    print("=" * 60)
    print("SETUP META GRAPH API CREDENTIALS")
    print("=" * 60)
    print()

    if not CRED_PATH.exists():
        print(f"ERRO: {CRED_PATH} nao existe. Rode do diretorio raiz do projeto.")
        sys.exit(1)

    print("[1/3] SHORT TOKEN")
    print("Vai no Graph API Explorer (developers.facebook.com/tools/explorer)")
    print("Copia o token do campo 'Access Token' (clique no icone copy)")
    print("Cola aqui e da enter:")
    short_token = input("Short Token > ").strip()
    if len(short_token) < 100:
        print(f"ERRO: token curto demais ({len(short_token)} chars). Esperado 200+")
        sys.exit(1)
    print(f"OK: {len(short_token)} chars, comeca com {short_token[:15]}")
    print()

    print("[2/3] APP SECRET")
    cred_preview = json.loads(CRED_PATH.read_text(encoding="utf-8"))
    saved_secret = cred_preview.get("app_secret", "").strip()
    if saved_secret and len(saved_secret) >= 20:
        print(f"Usando app_secret salvo em .credentials/meta-graph-api.json ({len(saved_secret)} chars)")
        app_secret = saved_secret
    else:
        print("Vai em developers.facebook.com > V4 Audit > App Settings > Basic")
        print("Clica 'Show' do App Secret (pede senha), copia, cola aqui:")
        app_secret = input("App Secret > ").strip()
        if len(app_secret) < 20:
            print(f"ERRO: app_secret curto demais ({len(app_secret)} chars)")
            sys.exit(1)
        print(f"OK: {len(app_secret)} chars")
    print()

    print("[3/3] Trocando short token por long-lived (60 dias)...")
    url = (
        "https://graph.facebook.com/v25.0/oauth/access_token?"
        f"grant_type=fb_exchange_token&client_id={APP_ID}&"
        f"client_secret={app_secret}&fb_exchange_token={short_token}"
    )
    try:
        with urllib.request.urlopen(url, timeout=20) as r:
            result = json.loads(r.read())
    except urllib.error.HTTPError as e:
        print(f"ERRO trocando token: HTTP {e.code}")
        print(e.read().decode()[:600])
        sys.exit(1)

    long_token = result["access_token"]
    expires = result.get("expires_in", 0)
    print(f"Long-lived OK: {len(long_token)} chars, expira em ~{expires//86400} dias")
    print()

    cred = json.loads(CRED_PATH.read_text(encoding="utf-8"))
    cred["access_token_long"] = long_token
    cred["app_secret"] = app_secret
    CRED_PATH.write_text(
        json.dumps(cred, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Salvo em {CRED_PATH}")
    print()

    print(f"Testando com business_discovery em @{TEST_TARGET}...")
    ig_id = cred["ig_business_account_v4"]
    fields = (
        f"business_discovery.username({TEST_TARGET})"
        "{username,name,followers_count,media_count,biography}"
    )
    test_url = (
        f"https://graph.facebook.com/v21.0/{ig_id}?"
        f"fields={urllib.parse.quote(fields)}&access_token={long_token}"
    )
    try:
        with urllib.request.urlopen(test_url, timeout=20) as r:
            data = json.loads(r.read())
        print()
        print("=" * 60)
        print("TESTE SUCESSO!")
        print("=" * 60)
        print(json.dumps(data, ensure_ascii=False, indent=2))
    except urllib.error.HTTPError as e:
        print(f"TESTE ERRO: HTTP {e.code}")
        print(e.read().decode()[:600])
        sys.exit(1)


if __name__ == "__main__":
    main()
