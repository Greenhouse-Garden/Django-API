from django.contrib import admin
from django.db import router
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url 

#Django REST framework
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

#users
from users.views import users as users_views
from users.views.login import UserLoginAPIView as login
from users.views.users import ProfileCompletionViewSet

#products
from products import views

router = DefaultRouter()
router.register(r'profile', ProfileCompletionViewSet, basename='profile')


urlpatterns = [
    #users paths
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token),
    path('users/', users_views.UserListView.as_view(), name='users'),
    path('users/login/', login.as_view(), name='login'),
    path('users/signup/', users_views.signup, name='signup'),
    path('users/verify/', users_views.account_verification, name='verify'),
    path('', include(router.urls)),

    #products paths
    path('products/create/', views.create, name='create'),
    path('products/list/', views.get_all, name='list'),
    path('products/get/<int:productId>/', views.get_one, name='get')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
