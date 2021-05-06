from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    
    path('login/', auth_views.LoginView.as_view(template_name='users/login.htm'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.htm'), name='logout'),
    path('', include('blog.urls')),
     path('profile/', user_views.profile, name='profile'),


]
