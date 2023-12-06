from fastapi.testclient import TestClient
from .main import app  # Import your FastAPI app


def test_db_connection():
    """
    Test that the database connection is working
    """
    conn = get_db_connection()
    assert conn is not None


def test_create_order():
    """
    Create a test order and write it to the database
    """
    test_order = {
        "product_name": "Tent",
        "quantity": 1,
        "total_price": 199.99,
        "customer_name": "test customer",
        "street_address": "test address",
        "state": "NC",
        "zip_code": 11111
    }

    order_id = write_order_to_db(test_order)
    print(order_id)
    assert isinstance(order_id, str)
    assert len(order_id) > 0


def test_get_order():
    """
    Create another test order and fetch it from the database
    """
    test_order = {
        "product_name": "Tent",
        "quantity": 1,
        "total_price": 199.99,
        "customer_name": "test customer",
        "street_address": "test address",
        "state": "NC",
        "zip_code": 11111
    }
    test_order_id = write_order_to_db(test_order)

    order = get_order_from_db(test_order_id)
    
    assert isinstance(order, dict)
    assert order["order_id"] == test_order_id
    assert order["product_name"] == "Tent"
    assert order["quantity"] == 1
    assert order["total_price"] == 199.99
    assert order["customer_name"] == "test customer"
    assert order["address"] == "test address, NC 11111"
    assert order["state"] == "NC"


def test_get_products():
    """
    Test that the get_products function returns a list of products
    """
    products = get_products()
    assert isinstance(products, dict)
    assert isinstance(products["products"], list)
    assert len(products["products"]) > 0
    assert isinstance(products["products"][0], dict)
    assert "product_name" in products["products"][0]
    assert "price" in products["products"][0]
    assert "description" in products["products"][0]
    assert "image" in products["products"][0]
    assert "num_in_stock" in products["products"][0]


def test_find_popular_products():
    """
    Test that the find_popular_products function returns a list of popular products
    """
    popular_products = find_popular_products(state="NC")
    assert isinstance(popular_products, list)
    assert len(popular_products) > 0
    assert isinstance(popular_products[0][0], str)
    assert isinstance(popular_products[0][1], int)
    assert popular_products[0][0] == "Tent"