#Overriding

from socket import gethostname, gethostbyname
from datetime import datetime
from enum import Enum
from uuid import uuid4


class Status(Enum):
    Active = 1
    Modified = 2
    Passive = 3


class BaseEntity:
    def __init__(self, name, description):
        self.id = uuid4()
        self.create_date = datetime.now()
        self.status = Status.Active.name
        self.ip_address = gethostname()
        self.machine_name = gethostbyname(gethostname())
        self.name = name
        self.description = description

    def show_info(self):
        print(f'Id: {self.id}\n'
              f'Name: {self.name}\n'
              f'Description: {self.description}\n'
              f'Status: {self.status}')


class Category(BaseEntity):
    pass


class Product(BaseEntity):
    def __init__(self, name, description, price, stock):
        super().__init__(name, description)
        self.price = price
        self.stock = stock

    def show_info(self):
        super().show_info()
        print(f'Price: {self.price}\n'
              f'Stock: {self.stock}')


category_instance = Category(input('Name: '), input('Description: '))
category_instance.show_info()
product_instance = Product(name=input('Name: '), description=input(('Description: ')), price=float(input('Price: ')), stock=float(input('Stock: ')))
product_instance.show_info()
