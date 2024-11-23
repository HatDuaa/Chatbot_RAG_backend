from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('process_message/', views.process_message, name='receive_data'),
    
]