from uuid import uuid4
from enum import Enum
from datetime import datetime
import socket


class Status(Enum):
    Active = 1
    Modified = 2
    Passive = 3


class BaseEntity:
    def __init__(self, name: str, description: str, price: float, stock: float):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.Id = str(uuid4())
        self.create_date = datetime.now()
        self.machine_name = socket.gethostname()
        self.created_ip = socket.gethostbyname(socket.gethostname())
        self.Status = Status.Active.name


class Product(BaseEntity):
    pass


class ProductService:
    def create_product(self, product: Product) -> None:
        products.append(product)
        print(f'{product.name} has just added successfully...! ')
        print(f'{product.name} has been added by {product.machine_name} computer.')
        print(f'Machine IP Address: {product.created_ip} computer.')

    def update_product(self, id: str, name: str, description: str, price: float, stock: float) -> None:
        for product in products:
            if product.Id == id:
                if product.name == ' ':
                    product.name = name
                if product.description == description:
                    product.description = description
                if price != price:
                    product.price = price
                if stock != stock:
                    product.stock = stock

                    product.Status = Status.Modified.name
                    product.create_date = datetime.now()
            print(f'It has been updated successfully...!')
            print(f'Ip Address: {product.created_ip} ')
            print(f'Update time: {product.create_date} ')

    def delete(self, id: str):
        for product in products:
            if product.Id == id:
                product.Status = Status.Passive.name
                print(f'{product.name} has been deleted by {product.machine_name} computer.')
                print(f'Machine IP Address: {product.created_ip}')

    def get_all_product_info(self) -> None:
        for product in products:
            if product.Status != Status.Passive.name:
                print(f'Id: {product.Id}\n'
                      f'Name: {product.name}\n'
                      f'Descripton: {product.description}\n'
                      f'Product Price: {product.price}\n'
                      f'Stock Quantity: {product.stock}\n'
                      f'Status: {product.Status}')

    def get_by_id(self, id: str) -> None:
        for product in products:
            if product.Id == id and product.Status != Status.Passive.name:
                print(f'Id: {product.Id}\n'
                      f'Name: {product.name}\n'
                      f'Descripton: {product.description}\n'
                      f'Product Price: {product.price}\n'
                      f'Stock Quantity: {product.stock}\n'
                      f'Status: {product.Status}')

    def get_by_name(self, name: str) -> None:
        for product in products:
            if product.name == name and product.Status != Status.Passive.name:
                print(f'Id: {product.Id}\n'
                      f'Name: {product.name}\n'
                      f'Descripton: {product.description}\n'
                      f'Product Price: {product.price}\n'
                      f'Stock Quantity: {product.stock}\n'
                      f'Status: {product.Status}')

    def get_by_price(self, under_price: float, over_price: float) -> None:
        for product in products:
            if under_price <= product.price <= over_price:
                print(f'Id: {product.Id}\n'
                      f'Name: {product.name}\n'
                      f'Descripton: {product.description}\n'
                      f'Product Price: {product.price}\n'
                      f'Stock Quantity: {product.stock}\n'
                      f'Status: {product.Status}')
    def get_by_stock(self, under_stock_quantity: float, over_stock_quantity: float):
        for product in products:
            if under_stock_quantity <= product.stock <= over_stock_quantity:
                print(f'Id: {product.Id}\n'
                      f'Name: {product.name}\n'
                      f'Descripton: {product.description}\n'
                      f'Product Price: {product.price}\n'
                      f'Stock Quantity: {product.stock}\n'
                      f'Status: {product.Status}')


products = []


def main():

    print('Menu: \n'
          'Create             ==> 1\n'
          'Update             ==> 2\n'
          'Delete             ==> 3\n'
          'Get All Info       ==> 4\n'
          'Get Info By Id     ==> 5\n'
          'Get Info By Name   ==> 6\n'
          'Get Info By Price  ==> 7\n'
          'Get Info By Stock  ==> 8\n'
          'Exit               ==> e')

    while True:
        process = input('Please choose your process: ')

        match process:
            case '1':
                name = input('Please type into product name: ')
                description = input('Please type into description of product: ')
                price = float(input('Please type into price: '))
                stock_quantity = float(input('Please type into stock quantity: '))

                new_product = Product(name, description, price, stock_quantity)
                product_creator = ProductService()
                product_creator.create_product(new_product)
            case '2':
                id = input('Please type into product id: ')
                name = input('Please type into product name: ')
                description = input('Please type into description of product: ')
                price = float(input('Please type into price: '))
                stock_quantity = float(input('Please type into stock quantity: '))
                ProductService().update_product(id, name, description, price, stock_quantity)
            case '3':
                id = input('Please type into product id: ')
                ProductService().delete(id)
            case '4':
                ProductService().get_all_product_info()
            case '5':
                id = input('Please type into product id: ')
                ProductService().get_by_id(id)
            case '6':
                name = input('Please type into product name: ').lower()
                ProductService().get_by_name(name)
            case '7':
                under_price = float(input('Please type under price: '))
                over_price = float(input('Please type over price: '))
                ProductService().get_by_price(under_price, over_price)
            case '8':
                under_stock = float(input('Please type under price: '))
                over_stock = float(input('Please type over price: '))
                ProductService().get_by_stock(under_stock, over_stock)
            case 'e':
                print('Application has been closed..! ')
                break
            case _:
                print('Please choose valid process...!')


main()


