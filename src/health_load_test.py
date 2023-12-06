from locust import HttpUser, task, between

class HealthCheckUser(HttpUser):
    wait_time = between(0.1, 0.3)  # Adjust this as needed

    @task
    def health_check(self):
        self.client.get("/health_check")