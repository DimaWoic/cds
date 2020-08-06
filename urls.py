from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('company/', views.CompanyIndex.as_view(), name='company'),
    path('add_company', views.CompanyCreate.as_view(), name='add_company'),
    path('company_units/', views.CompanyUnitsIndex.as_view(), name='company_units'),
    path('delete/<int:pk>', views.DelCompany.as_view(), name='del_company'),
    path('add_company_units', views.CompanyUnitCreate.as_view(), name='add_company_units'),
    path('del_company_units/<int:pk>', views.DelCompanyUnit.as_view(), name='del_company_units'),
    path('position/', views.PositionIndex.as_view(), name='positions'),
    path('add_position', views.PositionCreate.as_view(), name='add_position'),
    path('del_position/<int:pk>', views.DelPosition.as_view(), name='del_position'),
    path('workers/', views.WorkerIndex.as_view(), name='worker_index'),
    path('add_worker', views.WorkerCreate.as_view(), name='worker_add')
]