from django.contrib import admin
from django.urls import path, include
from .views import CompanyListAPI,CompanyDeleteAPI, DeviceDetailsAPI, DeviceLogDetailsAPI, EmployeeListAPI, DeviceListAPI , DeviceLogListAPI , EmployeeDeleteAPI , DeviceDeleteAPI , DeviceLogDeleteAPI,CompanyDetailsAPI,EmployeeDetailsAPI


urlpatterns = [
    
        # <========= Company urls =============> 
    
        path('company-list/', CompanyListAPI.as_view(), name='company-list'),
        path('company/detail/<int:id>/', CompanyDetailsAPI.as_view(), name='company-detail'),
        path('company/create/', CompanyListAPI.as_view(), name='company-create'),
        path('company/update/<int:id>', CompanyListAPI.as_view(), name='company-update'),
        path('company/delete/<int:id>/', CompanyDeleteAPI.as_view(), name='company-delete'),
        
        
        # <========= Employee urls =============> 
        
        path('employee-list/', EmployeeListAPI.as_view(), name='employee-list'),
        path('employee/detail/<int:id>/', EmployeeDetailsAPI.as_view(), name='employee-detail'),
         path('employee/create/', EmployeeListAPI.as_view(), name='employee-create'),
         path('employee/update/<int:id>', EmployeeListAPI.as_view(), name='employee-update'),
         path('employee/delete/<int:id>', EmployeeDeleteAPI.as_view(), name='employee-delete'),
         
         
         # <========= Device urls =============> 
         
        path('device-list/', DeviceListAPI.as_view(), name='device-list'),
        path('device/detail/<int:id>/', DeviceDetailsAPI.as_view(), name='device-detail'),
        path('device/create/', DeviceListAPI.as_view(), name='device-create'),
        path('device/update/<int:id>', DeviceListAPI.as_view(), name='device-update'),
        path('device/delete/<int:id>', DeviceDeleteAPI.as_view(), name='device-create'),
        
        
        # <========= Device Logs urls =============> 
                
        path('device-log-list/', DeviceLogListAPI.as_view(), name='device-log-list'),
        path('device-log/detail/<int:id>/', DeviceLogDetailsAPI.as_view(), name='device-log-detail'),
        path('device-log/create/', DeviceLogListAPI.as_view(), name='device-log-create'),
        path('device-log/update/<int:id>/', DeviceLogListAPI.as_view(), name='device-log-update'),
        path('device-log/delete/<int:id>/', DeviceLogDeleteAPI.as_view(), name='device-log-delete'),
        
        
]