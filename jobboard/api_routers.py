from rest_framework.routers import DefaultRouter
from jobs.views import JobViewSet
from applications.views import ApplicationViewSet
from users.views import UserViewSet

router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename='job')
router.register(r'applications', ApplicationViewSet, basename='application')
router.register(r'users', UserViewSet, basename='user')
