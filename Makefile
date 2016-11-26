python_version=2.7
python_cmd=python${python_version}
venv_name=.env
venv_cmd=virtualenv -p ${python_cmd} ${venv_name}
virtualenv=. ${venv_name}/bin/activate;

default: install

.env:
	${venv_cmd}
	${virtualenv} pip install -U setuptools

install: .env
	${virtualenv} pip install -e .

clean:
	@rm -rf .env
