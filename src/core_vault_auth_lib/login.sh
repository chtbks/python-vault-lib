#!/bin/sh

CB_VAULT_URI='https://secrets-api.chatbooks.com:8200'

echo "Please enter your username"
read USER
echo "Please enter your password"
read PASS

CB_VAULT_TOKEN=$(python3 core-vault-auth-lib.py -u USER -p PASS)
CB_VAULT_TOKEN=''

set -e
export CB_VAULT_URI
export CB_VAULT_TOKEN