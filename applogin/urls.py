from django.urls import path
from knox import views as knox_views
from .views import login_api, get_user_data, register_api

urlpatterns = [
    path('login/', login_api, name='login'),
    path('user/', get_user_data, name='user'),
    path('register/', register_api, name='register'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall')
]