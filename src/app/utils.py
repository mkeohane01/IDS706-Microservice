import pyodbc
from dotenv import load_dotenv
import os
load_dotenv()

def get_db_connection():
    connection = pyodbc.connect(
        'Driver={ODBC Driver 18 for SQL Server};'
        'Server=tcp:team-project-orders.database.windows.net,1433;'
        'Database=OrdersDB;'
        f'Uid={os.getenv("DB_USERNAME")};'
        f'Pwd={os.getenv("DB_PASSWORD")};'  
        'Encrypt=yes;'
        'TrustServerCertificate=no;'
        'Connection Timeout=30;'
    )
    return connection