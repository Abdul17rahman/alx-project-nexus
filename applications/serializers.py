from rest_framework import serializers
from .models import Application
from users.serializers import UserSerializer
from jobs.serializers import JobSerializer


class ApplicationSerializer(serializers.ModelSerializer):
    applicant = UserSerializer(read_only=True)
    job = JobSerializer(read_only=True)

    class Meta:
        model = Application
        fields = [
            'id', 'applicant', 'job', 'resume',
            'cover_letter', 'status', 'applied_at'
        ]
        read_only_fields = ['id', 'applicant', 'job', 'applied_at']
