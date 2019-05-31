from rest_framework import routers
from pets.views import PetsViewSet, UserViewSet
from django.conf.urls import url, include


router = routers.SimpleRouter()
router.register(r'pets', PetsViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls