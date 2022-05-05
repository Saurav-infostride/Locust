from locust import User, task, constant

#                                       Command to run
'''locust -f OnStartOnStopMethods\startstop_user.py -u 1 -r 1 -t 10s --headless --only-summary'''


class MyTest(User):
    wait_time = constant(1)

    '''this will run only start'''
    def on_start(self):
        print("Starting")

    @task
    def task_1(self):
        print("My tasks")

    '''this will run only at end'''
    def on_stop(self):
        print("Stopping")
