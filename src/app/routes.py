from flask import request, jsonify, render_template, redirect
from app import app
from app.utils import write_order_to_db, get_order_from_db, get_products, state_abbreviations


@app.route('/', methods=['GET', 'POST'])
def create_order():
    if request.method == 'POST':
        data = request.json
        order_id = write_order_to_db(data)
        print(f"New order! {order_id}")
        return jsonify({'message': 'Order created', 'order_id': order_id}), 201
    
    elif request.method == 'GET':
        data = get_products()
        return render_template('index.html', result=data, states=state_abbreviations)


@app.route('/orders/<string:order_id>', methods=['GET'])
def get_order(order_id):

    order = get_order_from_db(order_id)

    order_data = {
                'order_id': order_id,
                'product_name': order["product_name"],
                'quantity': order["quantity"],
                'total_price': order["total_price"],
                'customer_name': order["customer_name"],
                'address': order["address"],
                'popular_products': ["a", "b", "c"]
            }

    return render_template('view_order.html', result=order_data)


@app.route('/get_product', methods=['GET'])
def get_product():
    product_name = request.args.get('product_name')
    print(f"Product: {product_name}")
    data = get_products()
    
    for product in data["products"]:
        if product["product_name"] == product_name:
            return jsonify(product)
        
    return jsonify({'message': 'Product not found'}), 404

    
