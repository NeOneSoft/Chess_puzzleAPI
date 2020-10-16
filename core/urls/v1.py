# Django
from django.conf.urls import url, include

# Djangorestframework
from rest_framework import routers

# Views
from boards.views import BoardViewSet

# API urls
router = routers.DefaultRouter()
router.register(r'boards', BoardViewSet),

urlpatterns = [
    url(r'', include(router.urls)),
]
