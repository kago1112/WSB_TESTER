from locust import HttpUser, task

# klasy nalezy zaczynac od wielkiej litery
# @ (dekorator) - ????
class MyUser(HttpUser):
    @task
    def get_posts(self):
        self.client.get("/comments")

# locust -f locustfile.py --host=https://jsonplaceholder.typicode.com