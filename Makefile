install:
	@echo "Installing dependencies..."
	@pipenv install

setup: install
	@echo "Installing pre-commit hooks..."
	@pre-commit install
	@echo "Done!"

test:
	@echo "Running tests..."
	@pipenv run pytest -v

lint:
	@echo "Running linter..."
	@pylint --rcfile=.pylintrc src
