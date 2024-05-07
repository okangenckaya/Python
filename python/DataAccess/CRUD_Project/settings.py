from pymongo import MongoClient

conn = MongoClient('mongodb://localhost:27017')

db = conn['product_data']

connection = db['categories']


#region Seed Data

#We inserted dummy data here.

# category_seed_data = [
#     {'name': 'Boxing Gloves', 'description': 'Everlast Produce best boxing gloves.'},
#     {'name': 'Punching Bags', 'description': 'Everlast Produce best punching bags.'},
#     {'name': 'Protective equipment', 'description': 'Everlast Produce best protective equipment.'},
# ]
#
# connection.insert_many(category_seed_data)

#endregion

