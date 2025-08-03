from django.db import models
from users.models import User
from jobs.models import Job


class Application(models.Model):

    class application_status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        ACCEPTED = 'accepted', 'Accepted'
        REJECTED = 'rejected', 'Rejected'

    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE, related_name='applications')
    resume = models.FileField(blank=True, null=True, upload_to='resumes/')
    cover_letter = models.FileField(
        blank=True, null=True, upload_to='cover_letters/')
    status = models.CharField(
        max_length=10,
        choices=application_status.choices,
        default=application_status.PENDING
    )
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.email} - {self.job.title}"
