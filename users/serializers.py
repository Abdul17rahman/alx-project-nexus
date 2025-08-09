from rest_framework import serializers
from .models import User
from django.urls import reverse


class UserSerializer(serializers.ModelSerializer):

    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'email',
                  'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'date_joined', 'detail_url']
        read_only_fields = ('id', 'detail_url')

    def get_detail_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('user-detail', args=[obj.pk]))
