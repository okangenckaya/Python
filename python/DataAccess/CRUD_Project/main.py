from model import Category
from service import CategoryService
from bson.objectid import ObjectId


category_services = CategoryService()

print('Menu:\n'
      'Register        =>     1\n'
      'List            =>     2\n'
      'List by id      =>     3\n'
      'List by default =>     4\n'
      'Update          =>     5\n'
      'Delete          =>     6\n'
      'Exit            =>     e\n ')

while True:
    process = input('Please type your process: ')

    match process:
        case '1':
            # Create Category
            new_category = Category(name=input('Product Name: '), description=input('Product Description: '))
            # As Insert_one() function gets MongoDb data as dictionary,we converted argumants into dictonary.
            category_services.create(new_category.__dict__)

        case '2':
            # list of Categories
            for i in category_services.list():
                if i.get("status") != 3:
                    print(i)

        case '3':
            # list of Categories by id
            category_services.get_by_id(pk=input('id: '))

        case '4':
            # get by default
            filter_condition = input('Filter: ').lower()
            value = input('Value: ').lower()

            filter_value = {
                filter_condition: {'$regex': value}
            }

            category_services.get_default(filter_value)

        case '5':
            # update
            id = input('id: ')
            name = input('Name: ')
            description = input('Description: ')

            filter_keys = {
                '_id': ObjectId(id)
            }

            filter_value = {
                'name': name,
                'description': description,
                'status': 2
            }
            category_services.update(filter_keys, filter_value)
            print('Product has been updated successfully..! ')

        case '6':
            # delete
            id = input('id: ')

            filter_keys = {
                '_id': ObjectId(id)
            }

            filter_value = {'status': 3}

            category_services.delete(filter_keys, filter_value)
            print('Product has been removed...! ')

        case 'e':
            print('Application is closing...!')
            break
        case _:
            print('Please choose correct process...! ')

