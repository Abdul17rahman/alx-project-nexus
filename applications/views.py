from .serializers import ApplicationSerializer
from .models import Application
from rest_framework import viewsets
from .permissions import CanViewApplications


class ApplicationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing application instances.
    """
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [CanViewApplications]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff or user.is_superuser:
            return Application.objects.all()

        return Application.objects.filter(job__owner=user)

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)
