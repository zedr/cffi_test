python_version=3
python_cmd=python${python_version}
venv_name=.env
venv_cmd=${python_cmd} -m venv ${venv_name}
virtualenv=. ${venv_name}/bin/activate;
egg_link=${venv_name}/local/lib/${python_cmd}/site-packages/cffi-test.egg-link

default: install

${venv_name}:
	${venv_cmd}
	${virtualenv} pip install -U setuptools

${egg_link}: ${venv_name}
	${virtualenv} pip install -U pip
	${virtualenv} pip install wheel
	${virtualenv} pip install Cython
	${virtualenv} pip install -e .
	${virtualenv} python setup.py build_ext --inplace

install: ${egg_link}

perf: ${egg_link}
	${virtualenv} python scripts/perf.py

test: ${egg_link}
	${virtualenv} python src/cffi_test/tests.py

# We never use variables when calling rm -rf
clean:
	@rm -rf .env .eggs build src/*.egg-info
	@find src -name "*.pyc" -o -name "*.so" -exec rm "{}" \;
