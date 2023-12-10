from locust import task, between, FastHttpUser

class HealthCheckUser(FastHttpUser):
    """
    Test the health check endpoint. Simple GET request.
    """
    wait_time = between(0.01, 0.01)  # Adjust this as needed

    @task
    def health_check(self):
        self.client.get("/health_check")
