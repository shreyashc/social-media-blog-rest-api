from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from users.views import UserCreate, UserLogin, ChangePassword, UpdateProfie
from blog.views import CommentViewset, LikeViewset, SearchListView
from .views import home

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('comments', CommentViewset, basename='comments')
router.register('likes', LikeViewset, basename='likes')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('blogs/', include('blog.urls')),
    path('signup/', UserCreate.as_view(), name='signup'),
    path('login/', UserLogin.as_view(), name='login'),
    path('change-password/', ChangePassword.as_view(), name='cp'),
    path('update-profile/', UpdateProfie.as_view(), name='up'),
    path('search/', SearchListView.as_view(), name='search'),
    path('', home, name='home'),
]

urlpatterns += router.urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
