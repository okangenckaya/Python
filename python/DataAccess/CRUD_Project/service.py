from abc import ABC, abstractmethod
from settings import connection
from bson.objectid import ObjectId
from pymongo.errors import ConnectionFailure


class BaseService(ABC):

    @abstractmethod
    def create(self, item: dict): pass

    @abstractmethod
    def list(self): pass

    @abstractmethod
    def get_default(self, filter_values): pass

    @abstractmethod
    def get_by_id(self, pk): pass

    @abstractmethod
    def update(self, filter_key:dict, filter_value: dict): pass

    @abstractmethod
    def delete(self, filter_key: dict, filter_value: dict): pass


class CategoryService(BaseService):

    def create(self, item: dict):
        try:
            connection.insert_one(item)
            print('Category has been created successfully...! ')
        except TypeError:
            print('Please type into correct format! ')
        except ConnectionFailure:
            print('Category has not been created! ')

    def list(self):
        return connection.find()

    def get_default(self, filter_values: dict):
        for i in connection.find(filter_values):
            print(f'Name: {i.get("name")}\n'
                  f'Description: {i.get("description")}')

    def get_by_id(self, pk):
        items = connection.find({'_id': ObjectId(pk)})
        for i in items:
            print(f'Name: {i.get("name")}\n'
                  f'Description: {i.get("description")}')

    def update(self, filter_key: dict, filter_value: dict):
        return connection.update_one(filter_key, {'$set': filter_value})

    def delete(self, filter_key: dict, filter_value: dict):
        return connection.update_one(filter_key, {'$set': filter_value})






