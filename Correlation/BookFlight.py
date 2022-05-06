# Complete booking flow
####Launch new tours demo page - Create on_start task with get request
####Login with registered credential - task name login_demotour with post request
##verify through resp.text that user is on find flight page with post request
####Click continue with default value - task name find_flight with post request
##verify through resp.text that user is on select flight page with post request
####Click continue with default value - task name select_flight with post request
##verify through resp.text that user is on book flight page with post request
####Fill form with data & click secure purchase- task name book_flight with post request
##verify through resp.text that user gets booking confirmation with post request
# Run test with --logfile option to generate log file

from locust import TaskSet, task, between, HttpUser

UserName = [
    ("qamile1@gmail.com", "qa"),
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
