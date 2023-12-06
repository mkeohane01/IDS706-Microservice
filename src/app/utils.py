import pyodbc
from dotenv import load_dotenv
import os
import uuid
load_dotenv()


def get_db_connection():
    """
    Returns a connection to the database.
    """
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


def write_order_to_db(order):
    """
    Writes an order to the database and returns the ID of the newly created order.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    price = float(cursor.execute("SELECT price FROM PRODUCTS WHERE product_name=?", order["product_name"]).fetchone()[0])
    order_id = str(uuid.uuid4())

    cursor.execute("INSERT INTO ORDERS (order_id, product_name, quantity, total_price, customer_name, street_address, state, zip_code) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   order_id,
                   order["product_name"], 
                   order["quantity"], 
                   price * int(order["quantity"]),
                   order["customer_name"], 
                   order["street_address"],
                   order["state"],
                   order["zip_code"]
                   )
    conn.commit()
    conn.close()

    return order_id


def get_order_from_db(order_id):
    """
    Returns an order from the database.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ORDERS WHERE order_id=?", order_id)
    order = cursor.fetchone()

    conn.close()

    try:
        order_dict = {
            'order_id': order[0],
            'product_name': order[1],
            'quantity': order[2],
            'total_price': round(order[3],2),
            'customer_name': order[4],
            'address': f"{order[5]}, {order[6]} {order[7]}",
            'state': order[6]
        }
        return order_dict
    except TypeError:
        return {
            'order_id': "",
            'product_name': "",
            'quantity': 0,
            'total_price': 0,
            'customer_name': "",
            'address': ""
        }


def get_products():
    """
    Returns a list of all products in the database.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT product_name, price, description, image, num_in_stock FROM PRODUCTS")
    products = cursor.fetchall()

    conn.close()

    formatted_products = []
    for product in products:
        formatted_product = {
            'product_name': product[0],
            'price': product[1],
            'description': product[2],
            'image': product[3],
            'num_in_stock': product[4]
        }
        formatted_products.append(formatted_product)

    return {'products': formatted_products}


def find_popular_products(state):
    """
    Returns a list of the top 3 most popular products for a given state.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT TOP 3 product_name, COUNT(*) AS num_orders FROM ORDERS WHERE state=? GROUP BY product_name ORDER BY num_orders DESC", [state])
        products = cursor.fetchall()

        conn.close()
        return products
    except Exception as e:
        print(e)
        return []


state_abbreviations = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
]