from django.urls import path, include
from .views import UserView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', UserView)


urlpatterns = [
    path('', include(router.urls)),
]
