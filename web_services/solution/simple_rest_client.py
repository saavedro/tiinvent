# This script is example of code based interaction with webservices using `requests` library
# We use free toy service: http://dummy.restapiexample.com

# The service is an online HR system to store data about employees such as:
# employee_name, employee_salary, employee_age and profile_image

# Interaction with the service happens via http endpoints and json payloads

import requests
import argparse

# For more eye-friendly formatting
import pprint
pp = pprint.PrettyPrinter(indent=4)

service_url = "http://dummy.restapiexample.com/api/v1"

def get_employees():
    " Get all employees"
    print("INFO: Getting all entries")
    r = requests.get(service_url + "/employees")
    employee = r.json()
    return employee

def get_employee(_id):
    " Gets data of employee of give id from the ws"
    print("INFO: Getting info about employee id={}".format(_id))
    r = requests.get(service_url + "/employee/{}".format(_id))
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
    r = requests.post(service_url + "/create", json=employee_data)
    print("INFO: Response: {}, {}".format(r.status_code, r.text))
    try: # service returns error in not well defined JSON
        employee = r.json()
    except:
        return None
    return employee

def update_employee(_id, name, salary, age):
    " Update data of given employee "
    print("INFO: updating employee with id={}".format(_id))
    employee_new_data = {
        "name": name,
        "salary": salary,
        "age": age,
    }
    r = requests.put(service_url + "/update/{}".format(_id), json=employee_new_data)
    print("INFO: Response: {}, {}".format(r.status_code, r.text))
    employee = r.json()
    return employee

def delete_employee(_id):
    " Delete data of given employee"
    r = requests.delete(service_url + "/delete/{}".format(_id))
    print("Response: {}, {}".format(r.status_code, r.text))
    return r.text

if __name__ == "__main__":
    # Parsing args
    parser = argparse.ArgumentParser(description='Simple SAP HR client ;)')
    parser.add_argument('cmd', choices=['create', 'read', 'update', 'delete'], help="Action to be invoked")
    parser.add_argument('--id', "-i", action="store", help="employee id")
    parser.add_argument('--name', "-n", action="store", help="employee name")
    parser.add_argument('--age', "-a", action="store", help="employee age")
    parser.add_argument('--salary', "-s", action="store", help="emplyee salary")
    args = parser.parse_args()

    if args.cmd == "create":
        employee = create_employee(name=args.name, age=args.age, salary=args.salary)
        print("INFO: Employee data:")
        pp.pprint(employee)
    elif args.cmd == "read":
        # Id argument provided, query single entry
        if args.id:
            employee = get_employee(args.id)
            print("INFO: Employee data:")
            pp.pprint(employee) # Print two last entries
        else: # No id, get all entries
            employees = get_employees()
            print("INFO: Got #{} entries, Showing last two entries:")
            pp.pprint(employees[-2:]) # Print two last entries
    elif args.cmd == "update":
        if not args.id:
            raise Exception("Need to specify id to update an entry")
        update_employee(_id=args.id, name=args.name, age=args.age, salary=args.salary)
    elif args.cmd == "delete":
        if not args.id:
            raise Exception("Need to specify id to delete an entry")
        delete_employee(_id=args.id)
