from rest_framework.routers import DefaultRouter
from .views import BlogCustomUserViewSet

router = DefaultRouter()
router.register('', BlogCustomUserViewSet, basename='users')


urlpatterns = []
urlpatterns += router.urls
