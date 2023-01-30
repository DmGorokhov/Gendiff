install:
		poetry install

gendiff:
		poetry run gendiff

build:	check
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/*.whl

package-reinstall:
		python3 -m pip install --user --force-reinstall dist/*.whl

lint:
		poetry run flake8 gendiff

test:
		poetry run pytest

test-coverage:
		poetry run pytest --cov=gendiff --cov-report xml

test-cov:
		poetry run pytest --cov=gendiff

selfcheck:
		poetry check

check: selfcheck test lint

.PHONY: install test lint selfcheck check build
