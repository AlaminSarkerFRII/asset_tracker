from rest_framework import serializers
from .models import Company, Employee, Device, DeviceLog


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name','company_details',]
        readOnly_fields = ['id']


class EmployeeSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'company', 'company_name',]
        readOnly_fields = ['id']


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'type','serial_number','condition','company']
        readOnly_fields = ['id']


class DeviceLogSerializer(serializers.ModelSerializer):
    device_name = serializers.CharField(source='device_name.name', read_only=True)
    employee_name = serializers.CharField(source='employee_name.name', read_only=True)

    class Meta:
        model = DeviceLog
        fields = ['id','device_name', 'employee_name', 'check_out_at', 'check_in_at', 'condition_when_checked_out', 'condition_when_checked_at']
        
        read_only_fields = ['device_name', 'employee_name',]
    
    def create(self, validated_data):
        device_name = validated_data.pop('device_name')['name']
        employee_name = validated_data.pop('employee_name')['name']
        device = Device.objects.get(name=device_name)
        employee = Employee.objects.get(name=employee_name)
        
        device_log = DeviceLog.objects.create(device_name=device, employee_name=employee, **validated_data)
        
        return device_log