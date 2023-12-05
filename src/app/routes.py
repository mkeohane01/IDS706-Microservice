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

        data = {
            'products': [
                {
                    'product_name': 'Test Product',
                    'price': 10.45,
                    'description': "Test description....",
                    'image': 'https://images.unsplash.com/photo-1575378969004-967d6cfc4114?q=80&w=3474&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                    'num_in_stock': 1000
                },
                {
                    'product_name': 'Test Product 2',
                    'price': 0.01,
                    'description': "Test description 2....",
                    'image': 'https://media.licdn.com/dms/image/D5603AQEkhe4QiNksCA/profile-displayphoto-shrink_800_800/0/1698067367739?e=1707350400&v=beta&t=iez-cGAVpOWLKIGuNesIA1QWivYpmSzZJ7zXgLIx3aY',
                    'num_in_stock': 1
                }
            ]
        }
        return render_template('index.html', result=data)


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
    data = {
            'products': [
                {
                    'product_name': 'Test Product',
                    'price': 10.45,
                    'description': "Test description....",
                    'image': 'https://images.unsplash.com/photo-1575378969004-967d6cfc4114?q=80&w=3474&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                    'num_in_stock': 1000
                },
                {
                    'product_name': 'Test Product 2',
                    'price': 0.01,
                    'description': "Test description 2....",
                    'image': 'https://media.licdn.com/dms/image/D5603AQEkhe4QiNksCA/profile-displayphoto-shrink_800_800/0/1698067367739?e=1707350400&v=beta&t=iez-cGAVpOWLKIGuNesIA1QWivYpmSzZJ7zXgLIx3aY',
                    'num_in_stock': 1
                }
            ]
        }
    
    for product in data["products"]:
        if product["product_name"] == product_name:
            return jsonify(product)
        
    return jsonify({'message': 'Product not found'}), 404

    
