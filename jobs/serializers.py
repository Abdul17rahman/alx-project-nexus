from rest_framework import serializers
from .models import Job, JobCategory, JobType, Location
from users.serializers import UserSerializer


class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = ['id', 'name', 'slug', 'created_at']


class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = ['id', 'name', 'slug']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'city', 'state', 'country']


class JobSerializer(serializers.ModelSerializer):
    category = JobCategorySerializer(read_only=True)
    job_type = JobTypeSerializer(read_only=True)
    location = LocationSerializer(read_only=True)
    posted_by = UserSerializer(read_only=True)

    class Meta:
        model = Job
        fields = [
            'id', 'title', 'description', 'requirements', 'salary_range',
            'is_active', 'category', 'job_type', 'location', 'posted_by',
            'created_at', 'updated_at'
        ]

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        job_type_data = validated_data.pop('job_type')
        location_data = validated_data.pop('location')

        category, created = JobCategory.objects.get_or_create(**category_data)
        job_type, created = JobType.objects.get_or_create(**job_type_data)
        location, created = Location.objects.get_or_create(**location_data)

        job = Job.objects.create(
            **validated_data,
            category=category,
            job_type=job_type,
            location=location
        )
        return job
