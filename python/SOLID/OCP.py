"""
O - Open/Closed Principle
Software entities such as classes,modules, functions could be for extension. On the other hand,
it must be closed for modification. While a particular code can be remained for extension,it should be closed
for modification.

Let's give an example for OCP:

"""
from uuid import uuid4
category_lst = []


class BaseEntity:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


class CategoryServices:
    @staticmethod
    def create_category(category: BaseEntity):
        category_lst.append(category)

    @staticmethod
    def show_category():
        for i in category_lst:
            print(f'Category_Id: {i.id}\n'
                  f'Category Name: {i.name}\n'
                  f'Category Description: {i.description}')


def main():

    category_process = CategoryServices()
    category_name = input('Type category name: ')
    description = input('Type category description: ')
    category = BaseEntity(name=category_name, description=description, id=str(uuid4()))

    category_process.create_category(category)
    category_process.show_category()

main()

"""
In case we need show function according to id function, we can extend CategoryServices class.

"""

class CategoryServices:
    @staticmethod
    def create_category(category: BaseEntity):
        category_lst.append(category)

    @staticmethod
    def show_category():
        for i in category_lst:
            print(f'Category_Id: {i.id}\n'
                  f'Category Name: {i.name}\n'
                  f'Category Description: {i.description}')
    @staticmethod
    def show_detail_from_id(id):
        for i in category_lst:
            if i.id == id:
                print(f'Category_Id: {i.id}\n'
                      f'Category Name: {i.name}\n'
                      f'Category Description: {i.description}')


"""
We have extended the codes by not violating the other functions.

"""