from django.db import models
from users.models import User
from jobs.models import Job


class Application(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.TextField()
    cover_letter = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.email} - {self.job.title}"
