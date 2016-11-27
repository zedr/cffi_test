python_version=2.7
python_cmd=python${python_version}
venv_name=.env
venv_cmd=virtualenv -p ${python_cmd} ${venv_name}
virtualenv=. ${venv_name}/bin/activate;
egg_link=${venv_name}/local/lib/${python_cmd}/site-packages/cffi-test.egg-link

default: install

${venv_name}:
	${venv_cmd}
	${virtualenv} pip install -U setuptools

${egg_link}: ${venv_name}
	${virtualenv} pip install -e .

install: ${egg_link}

perf: ${egg_link}
	${virtualenv} python scripts/perf.py

test: ${egg_link}
	${virtualenv} python src/cffi_test/tests.py

# We never use variables when calling rm -rf
clean:
	@rm -rf .env .eggs build src/*.egg-info
