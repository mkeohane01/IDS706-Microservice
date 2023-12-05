from flask import request, jsonify, render_template
from app import app, db
from app.datapipe import Order


@app.route('/orders', methods=['GET', 'POST'])
def create_order():
    if request.method == 'POST':
        data = request.json
        new_order = Order(product_name=data['product_name'], quantity=data['quantity'], customer_name=data['customer_name'])
        db.session.add(new_order)
        db.session.commit()
        print(f"New order! {new_order.id}")
        return jsonify({'message': 'Order created', 'order_id': new_order.id}), 201
    elif request.method == 'GET':
        return render_template('index.html')


@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    # order = Order.query.get_or_404(order_id)
    # print(f"Order {order.id} retrieved")
    # TODO: Get order from databse. Check order id too. If id not valid, show invalid page. Also get popular products from pipeline. 
    order = {
        'product_name': 'Test Product',
        'quantity': 5,
        'price': 100,
        'customer_name': 'Test Customer',
        'address': '123 Test Street, NC 27502'
    }
    return render_template('view_order.html', result={
                                                'order_id': order_id,
                                                'product_name': order["product_name"],
                                                'quantity': order["quantity"],
                                                'price': order["price"],
                                                'customer_name': order["customer_name"],
                                                'address': order["address"],
                                                'popular_products': ["a", "b", "c"]
                                            })
