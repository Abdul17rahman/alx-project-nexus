from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from jobs.models import JobCategory, JobType, Location, Job
import random

User = get_user_model()


class Command(BaseCommand):
    help = 'Seed database with initial data'

    def handle(self, *args, **kwargs):

        categories = ["Engineering", "Design", "Marketing"]
        for cat in categories:
            JobCategory.objects.get_or_create(name=cat, slug=cat.lower())

        types = ["Full-time", "Part-time", "Contract"]
        for t in types:
            JobType.objects.get_or_create(
                name=t, slug=t.lower().replace(" ", "-"))

        locations = [
            {"city": "New York", "state": "NY", "country": "USA"},
            {"city": "Nairobi", "state": "Nairobi", "country": "Kenya"},
            {"city": "Kampala", "state": "Central", "country": "Uganda"},
        ]
        for loc in locations:
            Location.objects.get_or_create(**loc)

        admin = User.objects.get(username='Abdul')
        all_categories = JobCategory.objects.all()
        all_job_types = JobType.objects.all()
        all_locations = Location.objects.all()

        for i in range(10):
            Job.objects.create(
                title=f"Job Title {i+1}",
                description="This is a sample job description.",
                category=random.choice(all_categories),
                job_type=random.choice(all_job_types),
                location=random.choice(all_locations),
                posted_by=admin
            )

        self.stdout.write(self.style.SUCCESS('Seeded 10 job posts.'))
