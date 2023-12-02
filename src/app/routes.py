from flask import request, jsonify
from app import app, db
from app.datapipe import Order


@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    new_order = Order(product_name=data['product_name'], quantity=data['quantity'], customer_name=data['customer_name'])
    db.session.add(new_order)
    db.session.commit()
    print(f"New order! {new_order.id}")
    return jsonify({'message': 'Order created', 'order_id': new_order.id}), 201

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get_or_404(order_id)
    print(f"Order {order.id} retrieved")
    return jsonify({'product_name': order.product_name, 'quantity': order.quantity, 'customer_name': order.customer_name})
