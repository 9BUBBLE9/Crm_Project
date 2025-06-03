from django.urls import path
from . import views

urlpatterns = [
    path('', views.lead_list, name='lead_list'),
    path('create/', views.create_lead, name='create_lead'),
    path('update/<int:pk>/', views.lead_update, name='lead_update'),
    path('queue/<int:pk>/', views.add_to_queue, name='add_to_queue'),
]