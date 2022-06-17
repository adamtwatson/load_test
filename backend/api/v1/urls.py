from rest_framework.routers import DefaultRouter

from api.v1.viewsets.fast_viewset import FastViewset
from api.v1.viewsets.slow_viewset import SlowViewset

router = DefaultRouter()

router.register(prefix='fast', viewset=FastViewset, basename='fast')
router.register(prefix='slow', viewset=SlowViewset, basename='slow')

urlpatterns = router.urls
