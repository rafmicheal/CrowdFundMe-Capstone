from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Pledge(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='pledges')
    backer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='pledges')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.backer.username} pledged {self.amount} to {self.project.title}"
