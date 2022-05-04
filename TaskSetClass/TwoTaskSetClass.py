from locust import TaskSet, constant, task, HttpUser


class MyHTTPCat(TaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("Get Status of 200")
        self.interrupt(reschedule=False)

    '''Above "self.interrupt()" will help loop to get out-off first class and send it to other class'''


class MyAnotherHTTPCat(TaskSet):

    @task
    def get_status(self):
        self.client.get("/500")
        print("Get Status of 500")
        self.interrupt(reschedule=False)


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MyHTTPCat, MyAnotherHTTPCat]
    wait_time = constant(1)
