from locust import User, task, constant, HttpUser, SequentialTaskSet

#                                       Command to run
'''locust -f OnStartOnStopMethods\startstop_taskset.py -u 1 -r 1 -t 10s --headless --only-summary'''


class MyTest(SequentialTaskSet):
    '''this will run only start'''

    def on_start(self):
        self.client.get("/", name=self.on_start.__name__)
        print("Start")

    @task
    def browse_product_1(self):
        self.client.get("/product/OLJCESPC7Z", name=self.browse_product_1.__name__)
        print("Browse Product 1")

    @task
    def browse_product_2(self):
        self.client.get("/product/L9ECAV7KIM", name=self.browse_product_2.__name__)
        print("Browse Product 2")

    @task
    def cart_page(self):
        self.client.get("/cart", name=self.browse_product_2.__name__)
        print("Cart Page")

    '''this will run only at end'''

    def on_stop(self):
        self.client.get("/", name=self.on_stop.__name__)
        print("Stop")


class LoadTest(HttpUser):
    host = "https://onlineboutique.dev"
    tasks = [MyTest]
    wait_time = constant(1)
