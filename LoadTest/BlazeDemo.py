from locust import HttpUser, TaskSet, task


class LoginWithUniqueUsersSteps(TaskSet):

    @task
    def login(self):
        response = self.client.post("/login", {
            'email': 'LocustPerformanceUser1@gmail.com', 'password': '123567'
        })
        print(response.status_code)


class LoginWithUniqueUsersTest(HttpUser):
    tasks = [LoginWithUniqueUsersSteps]
    host = "http://blazedemo.com"

