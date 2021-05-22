from django.contrib import admin
from django.urls import path, include
from employee_register import views

urlpatterns = [
    path('', views.employee_form, name="employee_insert"),  #get and post req. for insert operation
    path('employee/<int:id>/', views.employee_form, name="employee_update"),  #get and post req. for update operation
    path('employee/delete/<int:id>/', views.employee_delete, name="employee_delete"), 
    path('employee/list', views.employee_list, name="employee_list"),   #get req. to retrieve and display all records
]
