install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	ruff check **/*.py

format:
	black **/*.py

test:
	pytest -vv ./src/app

load_test:
	locust -f src/health_load_test.py --headless --users 1000 --spawn-rate 100 --run-time 1m --host https://shopnozama.azurewebsites.net/

load_test_gui:
	locust -f src/health_load_test.py

load_test_datapipe_gui:
	locust -f src/load_test_data.py