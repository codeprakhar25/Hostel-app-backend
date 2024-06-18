from django.contrib import admin
from django.urls import path
from .views import GetUserView, SignupView, LoginView,UpdateUserView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('get-user/', GetUserView.as_view(), name='get-user'),
    path('update-user/', UpdateUserView.as_view(), name='get-user'),
]
