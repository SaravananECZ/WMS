# In your Django app's urls.py (e.g., warehouse_urls.py)

from django.urls import path
from .views import create_warehouse 
from . import views

urlpatterns = [
    path('create/', views.create_warehouse, name='create_warehouse'),
     path('search/', views.search_view, name='search'),
    # Add more URLs for other views as needed
]
