import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

    def __str__(self):
        return f"{self.name}, born on {self.dob}, {self.height} tall, from {self.city}, {self.state}"


with open("employee.json", "r") as f:
    employee_data = json.load(f)


employees = []
for employee in employee_data:
    name = employee["Name"]
    dob = employee["DOB"]
    height = employee["Height"]
    city = employee["City"]
    state = employee["State"]
    employees.append(Employee(name, dob, height, city, state))


for employee in employees:
    print(employee)
