from flask import request, jsonify, render_template, redirect
from app import app
import logging
from app.utils import write_order_to_db, get_order_from_db, get_products, find_popular_products, state_abbreviations


@app.route('/', methods=['GET', 'POST'])
def create_order():
    """
    On POST, creates a new order in the database using the user input from the frontend.

    On GET, fetches the list of products from the database and renders the index.html template.
    """
    if request.method == 'POST':
        try:
            data = request.json
            order_id = write_order_to_db(data)
            logging.info(f"New order created: {order_id}")
            return jsonify({'message': 'Order created', 'order_id': order_id}), 201
        except Exception as e:
            logging.error(f"Error creating order: {e}") 
            return jsonify({'message': 'Error creating order'}), 500
    
    elif request.method == 'GET':
        try:
            data = get_products()
            return render_template('index.html', result=data, states=state_abbreviations)
        except Exception as e:
            logging.error(f"Error fetching products: {e}") 
            return jsonify({'message': 'Error fetching products'}), 500


@app.route('/orders/<string:order_id>', methods=['GET'])
def get_order(order_id):
    """
    Uses the order_id to fetch the order from the database and render the view_order.html template.
    """
    try:
        order = get_order_from_db(order_id)
        popular_products = list(find_popular_products(state=order["state"]))

        order_data = {
                    'order_id': order_id,
                    'product_name': order["product_name"],
                    'quantity': order["quantity"],
                    'total_price': order["total_price"],
                    'customer_name': order["customer_name"],
                    'address': order["address"],
                    'popular_products': popular_products
                }

        return render_template('view_order.html', result=order_data)
    except Exception as e:
        logging.error(f"Error fetching order: {e}") 
        failed_order_data = {
                    'order_id': order_id,
                    'product_name': "Failed to Fetch",
                    'quantity': "Failed to Fetch",
                    'total_price': "Failed to Fetch",
                    'customer_name': "Failed to Fetch",
                    'address': "Failed to Fetch",
                    'popular_products': []
                }
        return render_template('view_order.html', result=failed_order_data)


@app.route('/get_product', methods=['GET'])
def get_product():
    """
    Fetches a product from the database using the product_name.
    """
    product_name = request.args.get('product_name')
    data = get_products()
    
    for product in data["products"]:
        if product["product_name"] == product_name:
            return jsonify(product)
        
    return jsonify({'message': 'Product not found'}), 404


@app.route('/health_check', methods=['GET'])
def health_check():
    """
    Simple health check endpoint.
    """
    return jsonify({'message': 'Healthy :)'}), 200

    