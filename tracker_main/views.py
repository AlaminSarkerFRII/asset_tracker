from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from rest_framework.permissions import DjangoModelPermissions

from .models import Company, Device, Employee, DeviceLog
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer


# ================= > Company List API view ================= >

class CompanyListAPI(APIView):
    permission_classes = []

    def get(self, request):
        result = {
                'status':  HTTP_200_OK,
                'message': 'Success',
                'data':    []
        }

        result_error = {
                'status':  HTTP_400_BAD_REQUEST,
                'message': 'Company Not Found',
                'data':    []
        }

        queryset = Company.objects.all()
        companies_serializer = CompanySerializer(queryset, many=True).data

        if companies_serializer:
            result['data'] = companies_serializer
            return Response(result)
        return Response(result_error)
    
    
    def post(self, request):
        result = {
                'status':  HTTP_200_OK,
                'message': 'Successfully created a company',
                'data':    []
        }

        result_error = {
                'status':  HTTP_400_BAD_REQUEST,
                'message': 'Bad Request or Invalid Request',
                'data':    []
        }
        
        serializer = CompanySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            result['data'] = serializer.data
            return Response(result)
        
        result_error['data'] = serializer.errors
        
        return Response(result_error)
    
    
    
    def put(self, request, id):
        result = {
                'status':  HTTP_200_OK,
                'message': 'Successfully company updated',
                'data':    []
        }

        result_error = {
                'status':  HTTP_400_BAD_REQUEST,
                'message': 'Company Not Found',
                'data':    []
        }
        
        company = Company.objects.get(id=id)
        
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            result['data'] = serializer.data
            return Response(result)
        
        result_error['data'] = serializer.errors
        return Response(result_error)
    

    
class CompanyDeleteAPI(APIView):
    permission_classes = []

    def get_queryset(self):
        return Company.objects.all()

    def delete(self, request, id):
        result = {
            'status': HTTP_200_OK,
            'message': 'Success',
        }

        company = self.get_queryset().filter(id=id).first()
        if company:
            company.delete()
            result['message'] = "Successfully Deleted Company"
        else:
            result['status'] = HTTP_404_NOT_FOUND
            result['message'] = "Company Not Found"

        return Response(result)

    
    


# ================= > Employee List API view ================= >

class EmployeeListAPI(APIView):
    
    permission_classes = []

    def get(self, request):
        result = {
                'status':  HTTP_200_OK,
                'message': 'Success',
                'data':    []
        }

        result_error = {
                'status':  HTTP_400_BAD_REQUEST,
                'message': 'Employee Not Found',
                'data':    []
        }

        queryset = Employee.objects.all()
        
        employee_serializer = EmployeeSerializer(queryset, many=True).data

        if employee_serializer:
            result['data'] = employee_serializer
            return Response(result)
        return Response(result_error)
    
    
    def post(self, request):
        result = {
                'status':  HTTP_200_OK,
                'message': 'Successfully created a Employee',
                'data':    []
        }

        result_error = {
                'status':  HTTP_400_BAD_REQUEST,
                'message': 'Bad Request or Invalid Request',
                'data':    []
        }
        
        serializer = EmployeeSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            result['data'] = serializer.data
            return Response(result)
        
        result_error['data'] = serializer.errors
        
        return Response(result_error)
    
    
    
    def put(self, request, id, *args, **kwargs):
        result = {
                'status':  HTTP_200_OK,
                'message': 'Successfully employee updated',
                'data':    []
        }

        result_error = {
                'status':  HTTP_400_BAD_REQUEST,
                'message': 'employee Not Found',
                'data':    []
        }
        
        employee = Employee.objects.get(id=id)
        
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            result['data'] = serializer.data
            return Response(result)
        
        result_error['data'] = serializer.errors
        return Response(result_error)
    
    

class EmployeeDeleteAPI(APIView):
    
    permission_classes = []

    def get_queryset(self):
        return Employee.objects.all()

    def delete(self, request, id):
        result = {
            'status': HTTP_200_OK,
            'message': 'Success',
        }

        employee = self.get_queryset().filter(id=id).first()
        
        if employee:
            employee.delete()
            result['message'] = "Successfully Deleted employee"
        else:
            result['status'] = HTTP_404_NOT_FOUND
            result['message'] = "employee Not Found"

        return Response(result)


# ================= > Device API view ================= >

class DeviceListAPI(APIView):
    permission_classes = []

    def get(self, request):
        result = {
                'status':  HTTP_200_OK,
                'message': 'Success',
                'data':    []
        }

        result_error = {
                'status':  HTTP_400_BAD_REQUEST,
                'message': 'Device Not Found',
                'data':    []
        }

        queryset = Device.objects.all()
        device_serializer = DeviceSerializer(queryset, many=True).data

        if device_serializer:
            result['data'] = device_serializer
            return Response(result)
        return Response(result_error)
    
    
    
    def post(self, request):
        result = {
                'status':  HTTP_200_OK,
                'message': 'Successfully created a Deviced',
                'data':    []
        }

        result_error = {
                'status':  HTTP_400_BAD_REQUEST,
                'message': 'Bad Request or Invalid Request',
                'data':    []
        }
        
        serializer = DeviceSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            result['data'] = serializer.data
            return Response(result)
        
        result_error['data'] = serializer.errors
        
        return Response(result_error)
    
    
    
    def put(self, request, id):
        
        result = {
                'status':  HTTP_200_OK,
                'message': 'Successfully Deviced updated',
                'data':    []
        }

        result_error = {
                'status':  HTTP_400_BAD_REQUEST,
                'message': 'device Not Found',
                'data':    []
        }
        
        device = Device.objects.get(id=id)
        
        serializer = DeviceSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            result['data'] = serializer.data
            return Response(result)
        
        result_error['data'] = serializer.errors
        return Response(result_error)
    
    
class DeviceDeleteAPI(APIView):
    
    permission_classes = []

    def get_queryset(self):
        return Device.objects.all()

    def delete(self, request, id):
        result = {
            'status': HTTP_200_OK,
            'message': 'Success',
        }

        device = self.get_queryset().filter(id=id).first()
        
        if device:
            device.delete()
            result['message'] = "Successfully Deleted Deviced"
        else:
            result['status'] = HTTP_404_NOT_FOUND
            result['message'] = "Deviced Not Found"

        return Response(result)


# ================= > Device Log API view ================= >

class DeviceLogListAPI(APIView):
    
    permission_classes = []

    def get(self, request, *args, **kwargs):
        result = {
                'status':  HTTP_200_OK,
                'message': 'Success',
                'data':    []
        }

        result_error = {
                'status':  HTTP_400_BAD_REQUEST,
                'message': 'Device Not Found',
                'data':    []
        }

        queryset = DeviceLog.objects.all()
        device_log_serializer = DeviceLogSerializer(queryset, many=True).data

        if device_log_serializer:
            result['data'] = device_log_serializer
            return Response(result)
        return Response(result_error)

     
    def post(self, request):
        result = {
                'status':  HTTP_200_OK,
                'message': 'Successfully created a Deviced Logs or Assignment',
                'data':    []
        }

        result_error = {
                'status':  HTTP_400_BAD_REQUEST,
                'message': 'Bad Request or Invalid Request',
                'data':    []
        }
        
        serializer = DeviceLogSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            result['data'] = serializer.data
            return Response(result)
        
        result_error['data'] = serializer.errors
        
        return Response(result_error)
    
    
    
    def put(self, request, id):
        
        result = {
                'status':  HTTP_200_OK,
                'message': 'Successfully Deviced Log updated',
                'data':    []
        }

        result_error = {
                'status':  HTTP_400_BAD_REQUEST,
                'message': 'device Not Found',
                'data':    []
        }
        
        device = DeviceLog.objects.get(id=id)
        
        serializer = DeviceLogSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            result['data'] = serializer.data
            return Response(result)
        
        result_error['data'] = serializer.errors
        return Response(result_error)
    
    
class DeviceLogDeleteAPI(APIView):
    
    permission_classes = []

    def get_queryset(self):
        return DeviceLog.objects.all()

    def delete(self, request, id):
        result = {
            'status': HTTP_200_OK,
            'message': 'Success',
        }

        device = self.get_queryset().filter(id=id).first()
        
        if device:
            device.delete()
            result['message'] = "Successfully Deleted Deviced Logs"
        else:
            result['status'] = HTTP_404_NOT_FOUND
            result['message'] = "Deviced Log Not Found"

        return Response(result)