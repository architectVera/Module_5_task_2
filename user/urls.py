from django.urls import path
from user.views import user_login, user_register

urlpatterns = [
    path('register/', user_register, name='u_register'),
    path('login/', user_login, name='u_login')
]