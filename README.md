# Asset-Tracker-App

The Asset Tracker System is a web application built using Django that enables companies to efficiently manage their corporate assets, such as phones, tablets, laptops, and other devices, which are handed out to employees. The application provides a streamlined way for companies to track the distribution, condition, and history of assets, ensuring effective asset management across different teams and departments.

## Features

- **Multi-Company Support**: The application is designed to accommodate multiple companies, allowing each company to manage their own set of employees and devices.

- **Employee and Device Management**: The system enables companies to add employees and devices to their profile. Employees can be associated with a specific company, and devices can be categorized by their name and condition.

- **Device Delegation**: Companies can delegate devices to employees for a specified period. The application enforces a check to ensure that devices are not delegated if they are already issued to an employee.

- **Device Log**: The system maintains a log of each device's checkout and return. It records the employee, condition, and timestamps of both actions.

- **API Support**: The application offers a RESTful API for managing companies, employees, devices, and device logs. This API allows developers to integrate asset tracking functionality into other systems.

## Getting Started

1. **Installation**: Clone this repository and Install the required dependencies using:

    ```bash
    pip install -r requirements.txt
    ```

2. **Database Setup**: Run database migrations using:

    ```bash
    python manage.py migrate
    ```

3. **Create Superuser**: Create a superuser to access the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

4. **Run Development Server**: Start the development server:

    ```bash
    python manage.py runserver

5. **Run For Testing**: For Test Case :

    ```bash
    python manage.py test
    ```

6. **Admin Panel**: Access the admin panel at `http://127.0.0.1:8000/admin/` to add companies, employees, devices, and manage device logs.

7. **API Endpoints**: Access the api root at 'api/' to manage assets programmatically. Refer to the API documentation for more details.


## API Documentation

The API provides the following endpoints:

- `api/company-list/`: List companies.
- `api/company/detail/<int:id>/`: Details of companies.
- `api/company/update/<int:id>/`: update specific company with id
- `api/company/create/<int:id>/`: Create company with id
- `api/company/delete/<int:id>/`: delete specific company with id


- `api/employee-list/`: List Employees.
- `api/employee/detail/<int:id>/`: Details of Employee.
- `api/employee/update/<int:id>/`: update specific Employee with id
- `api/employee/create/<int:id>/`: Create Employee with id
- `api/employee/delete/<int:id>/`: delete specific Employee with id

- `api/device-list/`: List Devices.
- `api/device/detail/<int:id>/`: Details of Device.
- `api/device/update/<int:id>/`: update specific Device with id
- `api/device/create/<int:id>/`: Create Device with id
- `api/device/delete/<int:id>/`: delete specific Device with id


- `api/device-log-list/`: List Devices Logs.
- `api/device-log/detail/<int:id>/`: Details of Device Log.
- `api/device-log/update/<int:id>/`: update specific Device Log with id
- `api/device-log/create/<int:id>/`: Create Device Log with id
- `api/device-log/delete/<int:id>/`: delete specific Device Log with id


