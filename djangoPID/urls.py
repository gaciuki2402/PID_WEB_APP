from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='djangoPID-index'),
    path('predictions/', views.predictions, name='djangoPID-predictions'),
]