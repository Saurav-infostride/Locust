from locust import HttpUser, task, constant

'''how we can leverage the command line options for the CI/CD and other purpose'''
#                                    Command to run
#                               DEBUG/INFO/WARNING/ERROR/CRITICAL
'''locust -f CommandLineDemo\RunTimeBasics.py -u 1 -r 1 -t 10s --headless --print-stats --csv Run1.csv --csv-full-history --host=https://example.com -L CRITICAL --logfile mylog.log --html Run1
    It will generate Log file'''


class MyLoadTest(HttpUser):
    wait_time = constant(1)

    @task
    def launch(self):
        # host = "https://http.cat.com"
        self.client.get("/")
