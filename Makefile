install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	ruff check *.py

format:
	black *.py

test:
	pytest -vv

load_test:
	locust -f load_test.py --headless --users 1000 --spawn-rate 100 --run-time 1m --host http://localhost:5000