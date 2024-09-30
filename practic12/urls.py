from django.urls import path
from .views import login_user, logout

urlpatterns = [
    path('login', login_user, name='login'),
    path('logout', logout, name='logout'),
]