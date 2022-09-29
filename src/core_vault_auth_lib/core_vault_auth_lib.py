import os
import hvac


class SecretsVault:
    client = None
    secrets = []  # static

    def login(self):
        print("Auth Not Found on CB_VAULT_TOKEN, or CB_VAULT_ROLE_ID & CB_VAULT_SECRET_ID\n")
        print("Please log in with your vault user/pass\n")
        print("Please enter your username\n")
        u = input()
        print("Please enter your password\n")
        p = input()
        self.authenticate(user=u, password=p)

    def authenticate(self, user=None, password=None, token=None):

        vaultUrl = os.getenv('CB_VAULT_URI', 'https://secrets-api.chatbooks.com:8200')

        if self.client is None or self.client.is_authenticated() is False:

            self.client = hvac.Client(url=vaultUrl)

            roleId = os.getenv('CB_VAULT_ROLE_ID')
            secretId = os.getenv('CB_VAULT_SECRET_ID')
            token = os.getenv('CB_VAULT_TOKEN', token)

            if roleId and secretId:

                self.client.auth.approle.login(
                    roleId,
                    secretId,
                )

            elif user and password:

                self.client.auth.userpass.login(user, password)
                selfToken = self.client.lookup_token()
                # print(selfToken)
                # print(selfToken['data']['id'])
                # self.client.renew_token(selfToken['data']['id'])
                os.environ['CB_VAULT_TOKEN'] = selfToken['data']['id']
                # print(selfToken['data']['id'])

            elif token:
                self.client.auth_cubbyhole(token)

            else:
                os.unsetenv('CB_VAULT_TOKEN')
                self.login()

    def get_secrets(self, envPath,
                    sharedPath=None, store='cb'):

        if len(self.secrets) > 0:
            return self.secrets

        self.authenticate()

        envPathKeys = {}
        combinedSecrets = {}

        if sharedPath:
            shared_secret_version_response = self.client.secrets.kv.v2.read_secret_version(
                path=sharedPath,
                mount_point=store
            )

            combinedSecrets = dict(shared_secret_version_response['data']['data'])

        secret_version_response = self.client.secrets.kv.v2.read_secret_version(
            path=envPath,
            mount_point=store
        )

        envPathKeys = dict(secret_version_response['data']['data'])

        for k, v in envPathKeys.items():
            combinedSecrets[k] = v

        SecretsVault.secrets = combinedSecrets

        # print(combinedSecrets)
        return combinedSecrets
