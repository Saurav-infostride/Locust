from locust import TaskSet, task, HttpUser, constant

UserName = [
    ("qamile1@gmail.com", "qamile"),
    ("kamile2@gmail.com", "qamile"),
    ("gamile3@gmail.com", "qamile"),
    ("wamile4@gmail.com", "qamile"),
    ("tamile5@gmail.com", "qamile")
]


class UserBehaviour(TaskSet):

    def on_start(self):
        self.userName = "Not_exist"
        self.password = "Not_exist"
        if len(UserName) > 0:
            self.userName, self.password = UserName.pop()

    @task
    def login_post(self):
        print(self.userName)
        self.client.post("/login.php", data={"action": "process", "userName": self.userName, "password": self.password
            , "login.x": "16", "login.y": "9"})


class User(HttpUser):
    tasks = [UserBehaviour]
    wait_time = constant(3)
    host = "http://newtours.demoaut.com"
