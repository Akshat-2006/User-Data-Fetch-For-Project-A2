from django.urls import path
from .views import register, dashboard
from django.contrib.auth import views as auth_views

app_name = 'myapp'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='inter_user/login.html'), name='login'),
    path('dashboard/', dashboard, name='dashboard'),
]