from locust import HttpUser, task, between, FastHttpUser

class HealthCheckUser(FastHttpUser):
    wait_time = between(0.01, 0.01)  # Adjust this as needed

    @task
    def health_check(self):
        self.client.get("/health_check")
