from django.contrib import admin
from django.urls import path, include
from .views import CompanyListAPI, EmployeeListAPI, DeviceListAPI , DeviceLogListAPI

urlpatterns = [
        path('company-list/', CompanyListAPI.as_view()),
        path('employee-list/', EmployeeListAPI.as_view()),
        path('device-list/', DeviceListAPI.as_view()),
        path('device-log-list/', DeviceLogListAPI.as_view()),
]