import getopt
import sys
import core_vault_auth_lib.core_vault_auth_lib as vault


def main():
    """Entry point for the application script"""

    if len(sys.argv) == 2:
        user, password = getopt.getopt(sys.argv, 'u:p:')
        v = vault.SecretsVault()
        v.authenticate(user, password)



