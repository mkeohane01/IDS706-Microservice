from locust import HttpUser, task, SequentialTaskSet, between
import random

# Assuming these utilities are adjusted for FastAPI
from app.utils import get_products, state_abbreviations

class OrderBehavior(SequentialTaskSet):
    states = state_abbreviations
    
    # Assuming get_products returns a list of product dictionaries
    products = get_products()

    def on_start(self):
        self.products = [product['product_name'] for product in self.products['products']]

    def generate_order_data(self):
        product_name = random.choice(self.products)
        state = random.choice(self.states)
        customer_name = f'test - {product_name} Buyer'
        street_address = f'{product_name} Street'
        zip_code = f'{random.randint(10000, 99999)}'
        # The data structure here should match your Pydantic OrderCreate schema
        return {
            'product_name': product_name,
            'quantity': 1,
            'total_price': 199.99,  # or any logic to calculate it
            'customer_name': customer_name,
            'address': street_address,
            'state': state
        }
    
    @task
    def post_order(self):
        data = self.generate_order_data()
        with self.client.post("/orders/", json=data, catch_response=True) as response:
            if response.status_code == 201:
                self.order_id = response.json()['order_id']
            else:
                response.failure(f"Failed to create order: {response.text}")

    @task
    def get_order(self):
        if hasattr(self, 'order_id'):
            with self.client.get(f"/orders/{self.order_id}", catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure("Failed to get order")

class OrderUser(HttpUser):
    tasks = [OrderBehavior]
    wait_time = between(0.1, 0.3)
