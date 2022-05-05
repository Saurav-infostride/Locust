from locust import user, task, constant, between, constant_pacing, User


class MyUser(User):
    # wait_time = constant(1)
    # wait_time = between(2, 5)
    wait_time = constant_pacing(3)

    @task
    def launch(self):
        print("This will inject the above described seconds delay")
