from rest_framework import serializers
from django.urls import reverse
from .models import Job, JobCategory, JobType, Location
from users.serializers import UserSerializer
from applications.serializers import ApplicationSerializer


class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = ['name']


class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = ['name']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['city', 'state', 'country']


class JobSerializer(serializers.ModelSerializer):
    category = JobCategorySerializer(read_only=True)
    job_type = JobTypeSerializer(read_only=True)
    location = LocationSerializer(read_only=True)

    owner = serializers.CharField(source='posted_by.username', read_only=True)

    application_count = serializers.SerializerMethodField()

    application_url = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = [
            'id', 'title', 'description', 'salary_range',
            'is_active', 'category', 'job_type', 'location', 'owner', 'application_count',
            'created_at', 'updated_at', 'application_url'
        ]

        read_only_fields = ('posted_by',)

    def get_application_count(self, obj):
        return obj.applications.count()

    def get_application_url(self, obj):
        request = self.context.get('request')
        # Assuming your Application create endpoint is at /api/applications/
        # and accepts 'job' in the POST body, so we just link to applications list/create endpoint.

        url = reverse('application-list')  # name from router registration
        if request is not None:
            return request.build_absolute_uri(url)
        return url
