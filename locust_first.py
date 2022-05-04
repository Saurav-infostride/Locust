from locust import User, task


class HelloWorldUser(User):

    @task
    def launch(self):
        print("Launching the URL")

    @task
    def search(self):
        print("Searching")


class MySecondTest(User):

    @task
    def launch2(self):
        print("Second Test")

    @task
    def search2(self):
        print("Second search test")
