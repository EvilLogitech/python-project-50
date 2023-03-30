install:
	poetry install

build:
	poetry build 

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user ./dist/*.whl

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff
	poetry run flake8 tests

c-lint:
	poetry run flake8 --max-cognitive-complexity=6 gendiff

test:
	poetry run pytest --cov

remove:
	python3 -m pip uninstall hexlet-code

test-coverage:
	poetry run pytest --cov=gendiff tests --cov-report xml

all: install build publish package-install check

rebuild: remove build package-install check

check: test test-coverage c-lint