from locust import HttpUser, task, SequentialTaskSet, between

class OrderBehavior(SequentialTaskSet):

    @task
    def post_order(self):
        data={
            "product_name": "Test Product",
            "quantity": 5,
            "customer_name": "Test Customer",
        }
        with self.client.post("/orders", json=data, catch_response=True) as response:
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
    wait_time = between(0.5, 1)
