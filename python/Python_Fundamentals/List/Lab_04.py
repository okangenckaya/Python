
# Creating student sign up:

from pprint import pprint

students = {}

while True:

    process = input('Please type your process you manage : ')

    match process:
        case 'exit':
            print('The application is closing now...!')
            break
    match process:

        case 'create':

            student_id = input('Please enter your student id given to you: ')
            identity_number = input('Please enter your identity number: ')
            name = input('Please enter your name: ')
            last_name = input('Please enter your last name: ')
            phone_number = (input('Please enter your phone number: '))
            mail = input('Please enter your mail address: ')

            students[student_id] = {
                'identity number': identity_number,
                'name': name,
                'last name': last_name,
                'phone number': phone_number,
                'mail address': mail
            }
        case 'read':
            pprint(students)

        case 'update':

            student_id = input('Please enter your student id: ')

            for key in students.keys():
                if key == student_id:
                    phone_number = int(input('Phone number: '))
                    mail = input('Mail address: ')

                    students.update(
                        {student_id: {
                            'phone number': phone_number,
                            'mail adress': mail
                        }
                    })
                    print('One register has been updated successfully...! ')
                    print(f'Student Id: {student_id}\n{students[student_id]}')
                else:
                    print("The student couldn't be found...! ")

        case 'delete':

            student_id = input('Please enter your student id: ')

            for key in students.keys():
                if key == student_id:
                    del students[student_id]
                    print('One register has been deleted...! ')
                    break
                else:
                    print("The student couldn't be found...! ")

        case _:
            print('Please enter a valid process...! ')

