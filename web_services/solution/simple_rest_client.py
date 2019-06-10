# This script example of code based interaction with webservices using requests library
# We use free toy service: http://dummy.restapiexample.com

# The service is an online HR system to store data about employees such as:
# employee_name, employee_salary, employee_age and profile_image

# Interaction with the service happens via http endpoints and json payloads

import requests
#import sys

# For more eye-friendly formatting
import pprint
pp = pprint.PrettyPrinter(indent=4)

# get all employees and show to last added ones
print("Getting all entries")
r = requests.get("http://dummy.restapiexample.com/api/v1/employees")
employees = r.json()
pp.pprint(employees[-2:]) # Get two last entries

print("Creating new entry")
payload = {
    "name": "Batman",
    "salary": 99999999,
    "age": 60,
}
r = requests.post("http://dummy.restapiexample.com/api/v1/create", json=payload)
print("Response: {}, {}".format(r.status_code, r.text))

# let's get our entry id!
try:
    _id = r.json()["id"]
except:
    print("New entry not created correctly, taking last for further processing")
    _id = employees[-1]["id"]

print("Getting our employee of interest: {}".format(_id))
r = requests.get("http://dummy.restapiexample.com/api/v1/employee/{}".format(_id))
print("Response: {}, {}".format(r.status_code, r.text))
employee = r.json() 
pp.pprint(employee)

