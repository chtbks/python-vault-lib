# Define required macros here
SHELL = /bin/sh

setup:
	python3 -m pip install --upgrade pip && pip install twine && python3 setup.py build

install:
	python3 setup.py install

build:
	python3 setup.py build

pip_install:
	python3 -m pip install --index-url https://pypi-registry.chatbooks.com/simple/ --upgrade build

pypy_upload:
	python3 setup.py sdist && \
	twine register dist/core_vault_auth_lib-1.0.0.tar.gz --repository cb && \
	twine upload --repository cb dist/*