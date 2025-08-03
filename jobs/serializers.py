from rest_framework import serializers
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

    class Meta:
        model = Job
        fields = [
            'id', 'title', 'description', 'salary_range',
            'is_active', 'category', 'job_type', 'location', 'owner', 'application_count',
            'created_at', 'updated_at'
        ]

        read_only_fields = ('posted_by',)

    def get_application_count(self, obj):
        return obj.applications.count()
