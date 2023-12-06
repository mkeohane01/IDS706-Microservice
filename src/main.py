from app import app  
import uvicorn
import logging

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

if __name__ == "__main__":
    uvicorn.run("src.app:app", host="0.0.0.0", port=5001, log_level="info")
