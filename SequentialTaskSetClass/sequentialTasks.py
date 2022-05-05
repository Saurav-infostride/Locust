from locust import SequentialTaskSet, HttpUser, constant, task

'''Class defining a sequence of tasks that a User will execute.
    In SequentialTaskSetClass class, all tasks are executed in order. Tasks can either be specified by
    setting the tasks attribute to a list of tasks, or by declaring tasks as methods using the @task decorator. The order
    of declaration decides the order of execution'''


class MySeqTask(SequentialTaskSet):
    @task
    def get_status(self):
        self.client.get("/200")
        print("Status of 200")

    @task
    def get_500_status(self):
        self.client.get("/500")
        print("Status of 500")

    @task
    def get_400_status(self):
        self.client.get("/400")
        print("Status of 400")


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MySeqTask]
    wait_time = constant(1)
