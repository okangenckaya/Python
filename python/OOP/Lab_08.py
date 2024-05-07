# Inheritance

class Person:
    age = 0
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        print("A person has been created...!")

    def read_data(self):
        return (f'First Name: {self.first_name}\n'
                f'Last Name: {self.last_name}\n'
                f'Age: {self.age}\n')


class Employee(Person):
    pass


e1 = Employee(first_name=input("First Name: "), last_name=input("Last Name: "))
e1.age = int(input("Age: "))
print(e1.read_data())




