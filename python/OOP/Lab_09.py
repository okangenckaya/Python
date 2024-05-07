from uuid import uuid4
from enum import Enum
from datetime import datetime

class Status(Enum):
    active = 1
    modified = 2
    passive = 3

class BaseEntity:
    def __init__(self, first_name: str, last_name: str, salary: int, department: str):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.department = department
        self.Id = str(uuid4())
        self.status = Status.active.name
        self.create_date = datetime.now()


class Employee(BaseEntity):
    pass


class Human_Resource(BaseEntity):

    def create_employee(self, employee: Employee) -> None:
        employees.append(employee)
        print(f'{employee.first_name} {employee.last_name} has been created..! ')

    def update_employee_data(self, id: str, first_name: str, last_name: str, department: str, salary: int, ) -> None:
        for employee in employees:
            if employee.Id == id:
                if first_name != ' ':
                    employee.first_name = first_name
                if last_name != ' ':
                    employee.last_name = last_name
                if department != ' ':
                    employee.department = department
                if salary != salary:
                    employee.salary = salary

                    employee.create_date = datetime.now()
                    employee.status = Status.modified.name
                    print("User data has been changed successfully...!")

    def delete_employee_data(self, id: str) -> None:
        for employee in employees:
            if employee.Id == id:
                employee.status = Status.passive.name

    def get_all_employee(self) -> None:
        for employee in employees:
            if employee.status != Status.passive.name:
                print(f"Id: {employee.Id}\n"
                      f"First Name: {employee.first_name}\n"
                      f"Last Name: {employee.last_name}\n"
                      f"Salary: {employee.salary}\n"
                      f"Department: {employee.department}\n"
                      f"Status: {employee.status}\n"
                      f"Create Date: {employee.create_date}\n"
                      f"---------------------------------------")


    def read_employee_by_id(self, id: str) -> None:
        for employee in employees:
            if employee.Id == id and employee.status != Status.passive.name:
                print(f"Id: {employee.Id}\n"
                      f"First Name: {employee.first_name}\n"
                      f"Last Name: {employee.last_name}\n"
                      f"Salary: {employee.salary}\n"
                      f"Department: {employee.department}\n"
                      f"Status: {employee.status}\n"
                      f"Create Date: {employee.create_date}\n"
                      f"---------------------------------------")

    def read_employee_by_full_name(self, full_name: str) -> None:
        for employee in employees:
            if f'{employee.first_name} {employee.last_name}'.__contains__(full_name) and employee.status != Status.passive.name:
                print(f"Id: {employee.Id}\n"
                      f"First Name: {employee.first_name}\n"
                      f"Last Name: {employee.last_name}\n"
                      f"Salary: {employee.salary}\n"
                      f"Department: {employee.department}\n"
                      f"Status: {employee.status}\n"
                      f"Create Date: {employee.create_date}\n"
                      f"---------------------------------------")



employees = []

def main():
    employee_1 = Employee('First', 'Employee', 5000, 'ARGE')
    employee_2 = Employee('Second', 'Employee', 6000, 'Internal Audit')

    employees.append(employee_1)
    employees.append(employee_2)

    hr = Human_Resource('HR', 'Employee', 5000, 'IK')

    print(f'Menu\n'
          f'Create Employee           ==> 1\n'
          f'List of Employee          ==> 2\n'
          f'Get Employee By Full Name ==> 3\n'
          f'Get Employee By Id        ==> 4\n'
          f'Update Employee           ==> 5\n'
          f'Delete Employee           ==> 6\n'
          f'Exit                      ==> e')

    while True:
        process = input('Choose your action upon menu: ')

        match process:
            case '1':
                first_name = input('First Name: ')
                last_name = input('Last Name: ')
                department = input('Department: ')
                salary = int(input('Salary: '))

                emp = Employee(first_name, last_name, salary, department)
                hr.create_employee(emp)

            case '2':
                hr.get_all_employee()
            case '3':
                full_name = input('Please type into full name: ')
                hr.read_employee_by_full_name(full_name)
            case '4':
                Id = input('Please type into Id: ')
                hr.read_employee_by_id(Id)
            case '5':
                id = input('Id: ')
                first_name = input('First Name:')
                last_name = input('Last Name:')
                department = input('Department: ')
                salary = int(input('Salary: '))


                hr.update_employee_data(id, first_name, last_name, department, salary)
            case '6':
                Id = input('Please type into id: ')
                hr.delete_employee_data(Id)
            case 'e':
                print('Application has been closed...! ')
                break

            case _:
                print('Please choose valid action..! ')



main()