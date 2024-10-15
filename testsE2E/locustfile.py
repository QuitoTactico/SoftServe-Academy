from locust import HttpUser, task

class SoftServeAcademy(HttpUser):
    @task
    def home(self):
        self.client.get("/")

    @task
    def learning_route(self):
        self.client.get("/learning_route")

    def on_start(self):
        self.client.post("/login", json={"email":"teteban0917@gmail.com", "password":"Teteban0917"})
