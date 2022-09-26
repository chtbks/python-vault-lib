import getopt
import sys


def main():
    """Entry point for the application script"""
    try:

        if len(sys.argv) == 2:
            user, password = getopt.getopt(sys.argv, 'u:p:')
            print('usage: args_demo.py -x <first_value> -b <second_value>')

    except getopt.GetoptError:
        print('about: ')
        print('usage: core_vault_auth_lib.py -u <user_name> -p <password> || response: <access_token>')
        sys.exit(2)
