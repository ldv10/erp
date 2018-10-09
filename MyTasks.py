from locust import TaskSet, task
import random
import string
class MyTasks(TaskSet):
    @task
    def simple_one(self):
        my_respone = ""
        with self.client.get('/', name='Test 1', catch_response=True) as response:
            try:
                my_respone = response
            except ValueError as e:
                response.failure('Could not get a response in json')
                return
            response.success()

