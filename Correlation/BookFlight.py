
from locust import TaskSet, task, between, HttpUser

UserName = [
    ("Jacob@gmail.com", "qa"),
]


class UserBehaviour(TaskSet):

    @task
    def on_start(self):
        self.userName = "Not_exist"
        self.password = "Not_exist"
        if len(UserName) > 0:
            self.userName, self.password = UserName.pop()

        res1 = self.client.post("login.php",
                                data={"action": "process", "userName": self.userName, "password": self.password})
        print(res1)

    @task(4)
    def find_flight(self):
        res2 = self.client.post("reservation.php")
        print(res2.text)


class User(HttpUser):
    tasks = [UserBehaviour]
    wait_time = between(5, 10)
    host = "https://demo.guru99.com/test/newtours/"
