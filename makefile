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
	python3 setup.py install && \
	python3 setup.py sdist && \
	twine upload --skip-existing --repository cb dist/*   --verbose