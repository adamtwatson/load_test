from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('v1/', include('api.v1.urls')),
] + router.urls

