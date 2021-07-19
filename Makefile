install:
	poetry install
brain-games:
	poetry run brain-games
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8 brain_games
brain-even:
	poetry run brain-even
package-reinstall:
	python3 -m pip install --force-reinstall dist/*.whl
build-reinstall:
	poetry build
	python3 -m pip install --force-reinstall dist/*.whl

