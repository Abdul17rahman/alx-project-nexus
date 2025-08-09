from django.contrib import admin
from django.urls import path, include
from jobboard.api_routers import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
