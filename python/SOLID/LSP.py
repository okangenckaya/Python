"""
L - Liskov's Substitution Principle

This principle states that objects of a superclass should be replaceable with objects of its subclasses without
affecting the correctness of the program. In other words, derived or child classes should be substitutable for their
base or parent classes in any context where the parent class is used. Moreover, Subclasses must be used in a way that
is accordant with their base or parent classes.

There is an example here:

"""

from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, age, education, salary):
        self.name = name
        self.age = age
        self.education = education
        self.salary = salary

    @abstractmethod
    def job_description(self) -> str: pass

    @abstractmethod
    def employee_details(self) -> dict: pass


class Developer(Employee):

    def __init__(self, name, age, education, salary, software_language):
        super().__init__(name, age, education, salary)
        self.software_language = software_language

    def job_description(self) -> str:
        return 'A developer can develop programs'

    def employee_details(self) -> dict:
        return self.__dict__


class HumanResources(Employee):

    def __init__(self, name, age, education, salary, strong_communication_ability):
        super().__init__(name, age, education, salary)
        self.strong_communication_ability = strong_communication_ability

    def job_description(self) -> str:
        return 'Human Resources are assigned to hire'

    def employee_details(self) -> dict:
        return self.__dict__


developer = Developer(name='first', age=28, education='Computer Science', salary=28000,
                      software_language=['Python', 'Java'])

hr = HumanResources(name='second', age=28, education='Business Administration', salary=18000,
                    strong_communication_ability=['Clear Writing', 'Critical Listening', 'Conflict Management'])

print(Developer.job_description(developer))
print(Developer.employee_details(developer))
print("-----------------------------------------------")
print(HumanResources.job_description(hr))
print(HumanResources.employee_details(hr))

"""
Each subclass has a distinct implementation of the job_description method, reflecting their unique roles. Attributes
such as 'software_language' and 'strong_communication_ability' are specific to their relevant subclasses, which is 
essential for their particular functionality. Finally, Both Developer and HumanResources can be used wherever an
Employee base class is expected without breaking the program. Therefore, this application does not violate LSP.
"""

