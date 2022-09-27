# This is a python package that takes care of loading secrets for an application at runtime

![Chatbooks Logo](https://chtbks.cdn.prismic.io/chtbks/6253092e-e5ba-4a11-943c-50efa4970d5c_chatbooks-logo-plum.svg "logo")

* pushable to private pypy repo
* login testable
* token auth testable
* approle auth testable

To install this package run

`pip install -i https://pypi-registry.chatbooks.com core_vault_auth_lib`

## for local development of your app you need to log in using your user/pass so run 

```bash
python3 core_vault_auth_lib login
```

## to access the secrets in your app
```python
import core_vault_auth_lib.core_vault_auth_lib as vault

v = vault.SecretsVault()
v.authenticate()
creds = v.get_secrets('job-server', store='bi')


```

[packaging guide]: https://packaging.python.org
[distribution tutorial]: https://packaging.python.org/tutorials/packaging-projects/
[chatbooks repository]: https://pypi-registry.chatbooks.com/

if you are building a new version make sure you have this file configured 

~/.pypirc 
```
[distutils]
index-servers =
    cb

[cb]
repository = https://pypi-registry.chatbooks.com/
username = cb
password = cb

```


