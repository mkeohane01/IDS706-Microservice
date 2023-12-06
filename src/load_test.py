from locust import HttpUser, task, SequentialTaskSet, between
import random
from app.utils import get_products, state_abbreviations

class OrderBehavior(SequentialTaskSet):

    states = state_abbreviations
    products = [product['product_name'] for product in get_products()['products']]

    def generate_order_data(self):
        product_name = random.choice(self.products)
        state = random.choice(self.states)
        customer_name = f'test - {product_name} Buyer'
        street_address = f'{product_name} Street'
        zip_code = f'{random.randint(10000, 99999)}'
        return {
            'product_name': product_name,
            'quantity': '1',
            'customer_name': customer_name,
            'street_address': street_address,
            'state': state,
            'zip_code': zip_code
        }
    
    @task
    def post_order(self):
        data = data = self.generate_order_data()
        with self.client.post("/", json=data, catch_response=True) as response:
            if response.status_code == 201:
                self.order_id = response.json()['order_id']
            else:
                response.failure("Failed to create order")

    @task
    def get_order(self):
        if hasattr(self, 'order_id'):
            self.client.get(f"/orders/{self.order_id}")
        else:
            self.interrupt()

class OrderUser(HttpUser):
    tasks = [OrderBehavior]
    wait_time = between(0.1, 0.3)
