from django.contrib import admin
from django.urls import path, include
from .views import CompanyListAPI,CompanyDeleteAPI, EmployeeListAPI, DeviceListAPI , DeviceLogListAPI


urlpatterns = [
        path('company-list/', CompanyListAPI.as_view()),
        path('company/create/', CompanyListAPI.as_view()),
        path('company/update/<int:id>', CompanyListAPI.as_view()),
        path('company/delete/<int:id>/', CompanyDeleteAPI.as_view(), name='company-delete'),
        
        path('employee-list/', EmployeeListAPI.as_view()),
        path('device-list/', DeviceListAPI.as_view()),
        path('device-log-list/', DeviceLogListAPI.as_view()),
        
        path('employees/<int:pk>/', EmployeeListAPI.as_view(), name='employee-detail'),
        path('devices/<int:pk>/', DeviceListAPI.as_view(), name='device-detail'),
        path('device-logs/<int:pk>/', DeviceLogListAPI.as_view(), name='device-log-detail'),
        
]