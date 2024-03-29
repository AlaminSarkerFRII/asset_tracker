from django.contrib import admin

from .models import Company, Employee, Device, DeviceLog


# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    model = Company
    fields = ['name']


admin.site.register(Company, CompanyAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    fields = ['name', 'company']


admin.site.register(Employee, EmployeeAdmin)


class DeviceAdmin(admin.ModelAdmin):
    model = Device
    fields = ['name', 'type','serial_number','condition','company']


admin.site.register(Device, DeviceAdmin)


class DeviceLogAdmin(admin.ModelAdmin):
    model = DeviceLog
    fields = ['id','device_name', 'employee_name', 'check_out_at', 'check_in_at', 'condition_when_checked_out', 'condition_when_checked_at']


admin.site.register(DeviceLog, DeviceLogAdmin)