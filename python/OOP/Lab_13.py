#Encapsulation

from uuid import uuid4
from datetime import datetime
from socket import gethostname, gethostbyname
from enum import Enum


class Status(Enum):
    Active = 1
    Modified = 2
    Passive = 3


class BaseEntity:
    def __init__(self):
        self.__id = ''
        self.__ip_address = ''
        self.__machine_name = ''
        self.__create_date = ''

    def set_values(self):
        self.__id = uuid4()
        self.__ip_address = gethostname()
        self.__machine_name = gethostbyname(gethostname())
        self.__create_date = datetime.now()

    def show_info(self):
        return self.__dict__


class Product(BaseEntity):
    def __init__(self, name, description):
        super().__init__()
        self.description = description
        self.name = name
        self.__stock = 0
        self.__price = 0

    def set_values_product(self,price, stock):
        super().set_values()
        if price > 0 and stock > 0:
            self.__price = price
            self.__stock = stock
            print('Product has been created..! ')
            print(self.__dict__)


name = input('Name: ')
description = input('Description: ')
price = float(input('Price: '))
stock = int(input('Stock: '))
p1 = Product(name, description)
p1.set_values_product(price, stock)
