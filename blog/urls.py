from rest_framework.routers import DefaultRouter
from .views import BlogViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('', BlogViewSet, basename='blogs')

urlpatterns = []
urlpatterns += router.urls
