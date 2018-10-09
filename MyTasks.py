from locust import TaskSet, task
import random
import string
class MyTasks(TaskSet):
    @task
    def simple_one(self):
        my_respone = dict()
        with self.client.get('/', name='Test 1', catch_respone=True) as response:
            try:
                my_respone = response.json()
            except ValueError as e:
                response.failure('Could not get a response in json')
                return
            response.success()
