from rest_framework import serializers
from .models import Company, Employee, Device, DeviceLog


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name','company_details', 'employees']
        readonly_fields = ['id']


class EmployeeSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'company', 'company_name','user']
        readonly_fields = ['id']


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
        readonly_fields = ['id']


class DeviceLogSerializer(serializers.ModelSerializer):
    device_name = serializers.CharField(source='device_name.name')
    employee_name = serializers.CharField(source='employee_name.name')

    class Meta:
        model = DeviceLog
        fields = ['device_name', 'employee_name', 'check_out_at', 'check_in_at', 'condition_when_checked_out', 'condition_when_checked_at']
        