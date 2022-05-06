import random
import re
import time
from locust import HttpUser, TaskSet, task, between

UserName = [
    ("JacobCreek", "Tester@123"),
]


class SubClassTest(TaskSet):

    @task
    def enterLoginCredentials(self):
        # res = self.client.post("login.php", data='''
        #         {username: "JacobCreek", password: "Tester@123"}
        #     ''')
        # print(res.text)
        # print(res.status_code)
        # print(res.headers)
        self.userName = "Not_exist"
        self.password = "Not_exist"
        if len(UserName) > 0:
            self.userName, self.password = UserName.pop()

        res1 = self.client.post("login.php",
                                data={"action": "process", "userName": self.userName, "password": self.password})
        if "Login Successfully" in res1.text and res1.elapsed.total_seconds() < 2.0:
            res1.success()
            print("HOOOOLLLLLLAAAAAA")
        else:
            print("Failed response time")
        print(res1.status_code)
        print(res1.headers)

    @task
    def find_flight(self):
        with self.client.post("reservation.php") as response:
            if response.elapsed.total_seconds() < 2.0:
                print("successfully")
                print(response.status_code)
                print(response.headers)
            else:
                print("Response time slow")

    @task
    def select_cruises(self):
        res3 = self.client.post("index.php")
        print(res3.status_code)
        print(res3.headers)


class MainClassTest(HttpUser):
    tasks = [SubClassTest]
    host = "https://demo.guru99.com/test/newtours/"
    wait_time = between(5, 10)
