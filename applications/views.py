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

        if user.is_superuser:
            return Application.objects.all()

        return Application.objects.filter(applicant=user)

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)

    def get_serializer_context(self):
        return {'request': self.request}
