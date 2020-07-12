from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('company/', views.company, name='company'),
    path('add_company', views.add_company, name='add_company'),
    path('company_units/', views.company_units, name='company_units'),
]