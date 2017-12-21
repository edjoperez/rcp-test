from django.conf.urls import url
from rest_framework import routers

from api.views import UserViewSet, get_date

router = routers.DefaultRouter()
router.register('usuarios', UserViewSet)
