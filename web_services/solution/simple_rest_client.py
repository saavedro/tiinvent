# This script is example of code based interaction with webservices using `requests` library
# We use free toy service: http://dummy.restapiexample.com

# The service is an online HR system to store data about employees such as:
# employee_name, employee_salary, employee_age and profile_image

# Interaction with the service happens via http endpoints and json payloads

import requests
#import sys

# For more eye-friendly formatting
import pprint
pp = pprint.PrettyPrinter(indent=4)

service_url = "http://dummy.restapiexample.com/api/v1/"

def get_employees():
    " Get all employees"
    print("INFO: Getting all entries")
    r = requests.get("http://dummy.restapiexample.com/api/v1/employees")
    employee = r.json()
    return employee

def get_employee(_id):
    " Gets data of employee of give id from the ws"
    print("INFO: Getting info about employee id={}".format(_id))
    r = requests.get("http://dummy.restapiexample.com/api/v1/employee/{}".format(_id))
    print("INFO: Response: {}, {}".format(r.status_code, r.text))
    employee = r.json()
    return employee

def create_employee(name, salary, age):
    "Creates employee of given data"
    print("INFO: Creating employee {}".format(name))
    employee_data = {
        "name": name,
        "salary": salary,
        "age": age,
    }
    r = requests.post("http://dummy.restapiexample.com/api/v1/create", json=employee_data)
    print("INFO: Response: {}, {}".format(r.status_code, r.text))
    employee = r.json()
    return employee

def update_employee(_id, name, salary, age):
    " Update data of given employee "
    print("INFO: updating employee with id={}".format(_id))
    employee_new_data = {
        "name": "Batman",
        "salary": salary,
        "age": 60,
    }
    r = requests.put("http://dummy.restapiexample.com/api/v1/update/{}".format(_id), json=employee_new_data)
    print("INFO: Response: {}, {}".format(r.status_code, r.text))
    employee = r.json()
    return employee

def delete_employee(_id):
    " Delete data of given employee"
    r = requests.delete("http://dummy.restapiexample.com/api/v1/delete/{}".format(_id))
    print("Response: {}, {}".format(r.status_code, r.text))
    return r.text

if __name__ == "__main__":
    pass
    #employees = get_employees()
    #pp.pprint(employees[-2:]) # Print two last entries

    #add_employee(

    # Let's give our employee a rise!
