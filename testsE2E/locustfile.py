from locust import HttpUser, task


class SoftServeAcademy(HttpUser):
    @task
    def home(self):
        self.client.get("/")

    @task
    def learning_route(self):
        self.client.get("/learning_route")

    @task
    def about(self):
        self.client.get("/about")

    @task
    def pricing(self):
        self.client.get("/pricing")

    @task
    def register(self):
        self.client.get("/register")


"""
    def on_start(self):
        self.client.post(
            "/login", data={"email": "teteban0917@gmail.com", "password": "Teteban0917"}
        )
"""
