
category_lst = []


class Category:

    def __init__(self, product_name: str, description: str):
        self.product_name = product_name
        self.description = description


class CategoryServices:

    def create_new_product(self, category: Category):
        category_lst.append(category)

    def read_information(self):
        for i in category_lst:
            print(f'Product Name: {i.product_name}\n'
                  f'Product Description: {i.description}\n')


def main():

    service_process = CategoryServices()

    print("Menu: \n"
          "Add a new product    ==> a\n"
          "Read the list        ==> r\n"
          "Exit                 ==> e\n")

    while True:
        process = input('Please choose the process: ').lower()

        match process:
            case 'a':
                product_name = input('Product Name: ')
                product_description = input('Description: ')
                category = Category(product_name=product_name, description=product_description)
                service_process.create_new_product(category)
            case 'r':
                service_process.read_information()
            case 'e':
                print('The application is closing...!')
                break
            case _:
                print('Please choose a valid process...! ')


main()

