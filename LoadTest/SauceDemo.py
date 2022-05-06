import random
import re
import time
from locust import HttpUser, TaskSet, task, between


class SubClassTest(TaskSet):

    @task
    def loginPage(self):
        self.client.get('/')

    @task
    def enterLoginCredentials(self):
        self.client.cookies.clear()
        url = "https://www.saucedemo.com/"
        data = {
            "username": "standard_user",
            "password": "secret_sauce",
            "signon": "Login"
        }
        with self.client.post(url, data=data, catch_response=True) as response:
            # print(response.text)
            # if "" in response.text:
            response.success()
            print(response)

            # try:
            #     random_product = re.findall(r"Catalog.action?viewCategory=&amp;categoryId=(.+?)\"",
            #                                 response.text)  # Extracting all the products
            #     self.random_product = random.choice(random_product)  # Storing the random product
            # except AttributeError:
            #     pass
        # else:
        #     response.failure("Sign in Failed")

    # def test_homePage(self):
    #     self.client.get('/inventory.html')
    #
    # def test_loginPage(self):
    #     self.client.get('cart.html')


class MainClassTest(HttpUser):
    tasks = [SubClassTest]
    host = "https://saucedemo.com"
    wait_time = between(5, 10)
