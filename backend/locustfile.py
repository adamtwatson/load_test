
import django
# setup needs to be first to allow django models to work
django.setup()

from locust import HttpUser, task, between
from data_processors.fast_processor import FastDataRepository
from data_processors.slow_processor import SlowDataRepository

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def fast_api(self):
        self.client.get("/api/v1/fast")

    @task
    def slow_api(self):
        self.client.get("/api/v1/slow")

    @task
    def fast_function_direct(self):
        # This wont show in the user interface but will still execute
        FastDataRepository().execute()

    # @task(3)
    # def view_items(self):
    #     for item_id in range(10):
    #         self.client.get(f"/item?id={item_id}", name="/item")
    #         time.sleep(1)

    # def on_start(self):
    #     self.client.post("/login", json={"username":"foo", "password":"bar"})