from locust import HttpUser, task, constant

'''how we can leverage the command line options for the CI/CD and other purpose'''
#                                    Command to run
'''locust -f CommandLineDemo\RunTimeBasics.py -u 1 -r 1 -t 10s --headless --print-stats --csv Run1.csv --csv-full-history --host=https://example.com
    It will generate exceptions, failures, stats and stats_history file'''


class MyLoadTest(HttpUser):
    wait_time = constant(1)

    @task
    def launch(self):
        # host = "https://http.cat.com"
        self.client.get("/")
