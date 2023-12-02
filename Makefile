install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	ruff check *.py

format:
	black *.py

test:
	pytest -vv
