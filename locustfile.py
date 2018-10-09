from locust import HttpLocust
from tasks import MyTasks
 class MyLocust(HttpLocust):
    task_set = MyTasks
    min_wait = 5000
    max_wait = 15000
    host = 'http://localhost:5000' 
