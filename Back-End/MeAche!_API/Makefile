.PYTHON: install format lint test sec

revisao: format lint

publicar: build upload

build:
	poetry build 

upload:
	twine upload dist/*

install:
	@poetry install

format:
	@blue .
	@isort .

lint:
	@blue --check .
	@isort --check .
	@prospector --with-tool pep257 --doc-warning

test:
	@pytest -v

sec:
	@pip-audit
