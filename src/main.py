from app import app
import logging

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)