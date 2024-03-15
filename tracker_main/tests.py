from django.test import TestCase
from .models import Company , Employee , Device , DeviceLog

# Create your tests here.
class CompanyTestCase(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name='Manufacturer Company', company_details='Manufacturer Company In Bangladesh')

    def test_company_creation(self):
        self.assertEqual(self.company.name, 'Manufacturer Company')
        self.assertEqual(self.company.company_details, 'Manufacturer Company In Bangladesh')
        
        
class EmployeeTestCase(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name='Alibaba')
        self.employee = Employee.objects.create(name='Kamrul Hasan', company=self.company)

    def test_employee_creation(self):
        self.assertEqual(self.employee.name, 'Kamrul Hasan')
        self.assertEqual(self.company.name, "Alibaba")


        
class DevicTestCase(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name='Alibaba')
        
        self.device = Device.objects.create(name='Dell Vestro', type='Desktop', serial_number="dh-0231", condition="good" , company=self.company)

    def test_device_creation(self):
        self.assertEqual(self.company.name, 'Alibaba')
        self.assertEqual(self.device.name, 'Dell Vestro')
        self.assertEqual(self.device.type, 'Desktop')
        self.assertEqual(self.device.serial_number, 'dh-0231')
        self.assertEqual(self.device.condition, 'good')
       
    