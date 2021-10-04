from locust import HttpUser, TaskSet, task, between

class UserTasks(TaskSet):
	@task(1)
	def index(self):
		self.client.post("/")

class WebsiteUser(HttpUser):
	tasks = [UserTasks]
	wait_time = between(1, 5)
