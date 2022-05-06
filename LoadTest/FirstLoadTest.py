import time
from locust import HttpUser, TaskSet, task, between


class SubClassTest(TaskSet):

    @task
    def infoIndia(self):
        self.client.get('/wiki/India')

    @task(2)
    def infoSpain(self):
        self.client.get('/wiki/Spain')


class MainClassTest(HttpUser):
    tasks = [SubClassTest]
    host = "https://id.wikipedia.org"
    wait_time = between(5, 10)
