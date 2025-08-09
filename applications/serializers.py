from rest_framework import serializers
from .models import Application
from users.serializers import UserSerializer


class ApplicationSerializer(serializers.ModelSerializer):
    applicant = UserSerializer(read_only=True)
    job = serializers.PrimaryKeyRelatedField(
        queryset=Application._meta.get_field('job').related_model.objects.all())

    class Meta:
        model = Application
        fields = [
            'applicant', 'job', 'resume',
            'cover_letter', 'status', 'applied_at'
        ]
        read_only_fields = ['id', 'applicant', 'applied_at', 'status']

    def validate(self, data):
        user = self.context['request'].user
        job = data['job']

        if not job.is_active:
            raise serializers.ValidationError("This job is no longer active.")

        if job.posted_by == user:
            raise serializers.ValidationError(
                "You cannot apply for your own job.")

        if user.is_superuser:
            raise serializers.ValidationError("Admins cannot apply for jobs.")

        if Application.objects.filter(applicant=user, job=job).exists():
            raise serializers.ValidationError(
                "You have already applied for this job.")

        return data

    def create(self, validated_data):
        user = self.context['request'].user
        return Application.objects.create(applicant=user, **validated_data)
