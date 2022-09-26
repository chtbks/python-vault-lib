# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest
import os
import core_vault_auth_lib.core_vault_auth_lib as vault


class TestSimple(unittest.TestCase):

    def test_login_with_user_pass(self):
        v = vault.SecretsVault()
        v.authenticate('unittest', 'f@HFV8LHg4mmVq*82vSvHb$KfF7^')
        secrets = v.get_secrets('unit', store='vault_unit_test')
        self.assertEqual(secrets['test'], 'test')
        token = os.getenv('CB_VAULT_TOKEN')
        self.assertIsNotNone(token, None)

        # auth with token now
        v.authenticate(token=token)
        secrets = v.get_secrets('unit', store='vault_unit_test')
        self.assertEqual(secrets['test'], 'test')

    def test_login_app_role(self):
        os.environ['CB_VAULT_ROLE_ID'] = '4816b607-76ce-a5cd-c229-09d87b76f49c'
        os.environ['CB_VAULT_SECRET_ID'] = 'c2a6b10d-3abb-644d-902d-7fd8b829fdf3'
        v = vault.SecretsVault()
        v.authenticate()
        secrets = v.get_secrets('unit', store='vault_unit_test')
        self.assertEqual(secrets['test'], 'test')


if __name__ == '__main__':
    unittest.main()
