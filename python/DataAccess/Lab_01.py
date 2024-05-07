
#region Establish a connection string

#Step 1: So as to communicate with MongoDb server, we need pymongo module.
from pymongo import MongoClient
from pprint import pprint

#Step 2: Creating connection string. We need a code that enables us to communicate with server.

conn = MongoClient('mongodb://localhost:27017')


#Step 3: Creating data base

db = conn['node_app']

#Step 4: We create a collection after we created data base.

collection = db['products']

# region Create a single record

product_name = input('Name: ')
price = input('Price: ')

product = {
    'name': product_name,
    'price': price

}

result = collection.insert_one(product)
print(result.inserted_id)
print(result.acknowledged)

# endregion

#region Create a multiple record

product_list = [
    {'_id': 1, 'name': 'Lenovo X1 Carbon', 'Price': 56.99},
    {'_id': 2, 'name': 'Macbook Pro M2', 'Price': 89.99},
    {'_id': 3, 'name': 'Asus Zenbook 6', 'Price': 46.69},
    {'_id': 4, 'name': 'Monster Alba', 'Price': 19.99},
    {'_id': 5, 'name': 'HP Radeon 3', 'Price': 29.99},
]
collection.insert_many(product_list)

# endregion

#region Read Record

results = collection.find()

for i in results:
    pprint(i)

# endregion

#region Find price greater than or equal to 30.00

filter_input = {
    'Price': {
        '$gt': 30.00
    }
}

results = collection.find(filter_input)
for i in results:
    print(i)
#endregion


#region Find price taken by user

price = float(input('Price: '))
for i in collection.find({'Price': {'$eq': price}}):
    print(i)
#endregion

#region Find price lower than or equal to 39.99

for i in collection.find({'Price': {'$lte': 33.99}}):
    print(i)

#endregion


#region Find a product including 'l' letter with regex

for item in collection.find({'name': {'$regex': 'L'}}):
    pprint(item)

#endregion

#region Update Record

result = collection.update_one(
    {'name': 'HP Radeon 3'},
    {'$set': {
        'name': 'Dell V2',
        'Price': '69.99'
    }
     }
)
print(f'{result.modified_count} amount record has been updated..!')

#endregion

#region Delete Record

collection.delete_one({'name': 'Monster Alba'})

#endregion

