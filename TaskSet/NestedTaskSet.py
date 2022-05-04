from locust import TaskSet, constant, task, HttpUser


class MyHTTPCat(TaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("Get Status of 200")

    '''The problem in Nested TaskSet is that once it gets into the Nested TaskSet, it keeps executing
        Nested class, it never goes back to parent class.
        So, in order to execute out of this class, we have to use "self.interrupt()"
        "reschedule=False", will add the breath time between parent and nested class '''
    @task
    class MyAnotherHTTPCat(TaskSet):

        @task
        def get_status(self):
            self.client.get("/500")
            print("Get Status of 500")
            self.interrupt(reschedule=False)


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MyHTTPCat]
    wait_time = constant(1)
