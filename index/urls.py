from django.urls import path, include
from . import views

app_name = 'index'

urlpatterns = [
    path('main/', views.main)
]
print("hello")