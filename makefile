# Define required macros here
SHELL = /bin/sh

install_pip:
	python3 -m pip install --upgrade pip

setup:
	pip install twine

install:
	python3 setup.py install

build:
	python3 setup.py build

pip_install:
	python3 -m pip install --index-url https://pypi-registry.chatbooks.com/simple/ --upgrade build

pypy_upload:
	python3 setup.py sdist &&  python3 -m twine upload --repository https://pypi-registry.chatbooks.com/simple/ dist/*
