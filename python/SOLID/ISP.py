"""
I - Interface Segregation Principle

This principle states that interfaces shouldn't include methods that are irrelevant to their clients. In other words,
clients shouldn't be forced to use methods they do not use. Interfaces must be suited to particular purposes.
There is an example here:

"""

"""
While the HRServices class includes attributes and functions related to personnel management based on the 
BasePersonnel model, the ProductServices class encapsulates attributes and functions specific to product management 
based on the BaseProduct model. So, this algorithm does not interface segregation principle.
"""

from uuid import uuid4
from enum import Enum

product_lst = []
personnel_lst = []


class Status(Enum):
    Active = 1
    Modified = 2
    Passive = 3


class BaseProduct:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.product_id = str(uuid4())
        self.status = Status.Active.name


class BasePersonnel:
    def __init__(self, first_name, last_name, job_description, birth_date, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.job_description = job_description
        self.birth_date = birth_date
        self.salary = salary
        self.id = str(uuid4())
        self.status = Status.Active.name


class ProductServices:

    @staticmethod
    def create_product(product: BaseProduct):
        product_lst.append(product)

    @staticmethod
    def show_details():
        for product in product_lst:
            if product.status != Status.Passive.name:
                print(f"Product Name: {product.name}\n"
                      f"Product Description: {product.description}\n"
                      f"Product Id: {product.product_id}\n"
                      f"Status: {product.status}")

    @staticmethod
    def update_product(id: str, product_name, description):
        for product in product_lst:
            if product.product_id == id:
                product.name = product_name
                product.description = description
                product.status = Status.Modified.name
                print(f"Product {product.name} updated. ")

    @staticmethod
    def delete_product(id: str):
        for product in product_lst:
            if product.product_id == id:
                product.status = Status.Passive.name
                print(f"Product {product.name} deleted. ")


class HRServices:

    @staticmethod
    def create_personnel(personnel: BasePersonnel):
        personnel_lst.append(personnel)

    @staticmethod
    def show_details():
        for personnel in personnel_lst:
            if personnel.status != Status.Passive.name:
                print(f"Personnel Name: {personnel.first_name}\n"
                      f"Product Surname: {personnel.last_name}\n"
                      f"Personnel Id: {personnel.id}\n"
                      f"Status: {personnel.status}\n"
                      f"Personnel Salary: {personnel.salary}\n"
                      f"Personnel Birthdate: {personnel.birth_date}\n"
                      f"Personnel's Position: {personnel.job_description}")

    @staticmethod
    def update_personnel(id: str, first_name, last_name, job_description, salary):
        for personnel in personnel_lst:
            if personnel.product_id == id:
                if personnel.first_name == first_name:
                    personnel.first_name = first_name
                if personnel.last_name == last_name:
                    personnel.last_name = last_name
                if personnel.salary != salary:
                    personnel.salary = salary
                if personnel.job_description != job_description:
                    personnel.job_description = job_description

                    personnel.status = Status.Modified.name

    @staticmethod
    def delete_personnel(personnel_id: str):
        for personnel in personnel_lst:
            if personnel.id == personnel_id:
                personnel.status = Status.Passive.name
                print(f"Personnel {personnel.first_name} {personnel.last_name} removed. ")


print('--------------------------------')
product = BaseProduct(name='first', description='description')
ProductServices.create_product(product)
ProductServices.show_details()
print('--------------------------------')
personnel = BasePersonnel(first_name='name', last_name='surname', job_description='job',
                          salary=000000, birth_date='birth date')
HRServices.create_personnel(personnel)
HRServices.show_details()
print('--------------------------------')

