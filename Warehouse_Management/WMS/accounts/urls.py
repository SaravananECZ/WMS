from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('create-account/<str:email>/', views.create_account, name='create_account'),
    path('login/', views.login, name='login'),
    # Other paths as needed
]
