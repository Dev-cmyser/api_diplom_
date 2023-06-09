from demo import views
from django.urls import path
from django.contrib.auth import views as auth_views
from demo.views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # path('login/', views.login),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),

    path('', about, name='about'),
    path('contact', contact, name='contact'),
    path('tasks', tasks, name='tasks'),
     path('accounts/register', RegistrationView.as_view(), name='register'),
    path('accounts/login', LoginView.as_view(), name='register'),
    path('accounts/logout', LogoutView.as_view(), name='register'),
    path('accounts/change-password', ChangePasswordView.as_view(), name='register'),
    path('accounts/token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('create-task/', add_task, name='add_task'),
    path('all-tasks/', view_tasks, name='view_tasks'),
    path('update/<int:pk>/', update_task, name='update_task'),
    path('item/<int:pk>/delete/', delete_task, name='delete_task'),

]
