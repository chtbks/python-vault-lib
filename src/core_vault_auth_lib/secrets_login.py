import os
import core_vault_auth_lib.core_vault_auth_lib as vault


def login():
    token = os.getenv('CB_VAULT_TOKEN')
    v = vault.SecretsVault()

    if token is not None:
        print("Please enter your username")
        u = input()
        print("Please enter your password")
        p = input()
        v.authenticate(u, p)
    else:
        v.authenticate()
