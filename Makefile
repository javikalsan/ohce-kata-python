.PHONY: default run coverage tests mutations

default:
	@printf "$$HELP"

run:
	python src/main.py

coverage:
	python -m pytest -vvv --cov=src/ohce
	coverage html
	@printf "Please open the report at htmlcov/index.html\n"

tests:
	python -m unittest tests/ohce/test*

mutations:
	mutmut run --paths-to-mutate src/ohce || true
	mutmut results

define HELP
 Local commands
	- make run\t\tRun locally using Python3
	- make coverage\t\tRun the test coverage using Python3
	- make tests\t\tRun tests locally using Python3
	- make mutations\tRun mutation tests locally using Python3
endef

export HELP
