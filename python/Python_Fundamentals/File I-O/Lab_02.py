
def exam_grades() -> None:
    file = open(file='exam_grades.txt', mode='w', encoding='utf-8')
    file.close()


def taking_data_from_student(first_name: str, last_name: str, midterm: float, final: float, homework: float) -> None:

    with open(file='exam_grades.txt', mode='a', encoding='utf-8') as file:
        file.write(f'{first_name} {last_name}:{midterm},{final},{homework}')


def exam_calculator(row: str) -> str:

    values = row.split(':')

    full_name = values[0]

    grades_list = values[1].split(',')

    ort = float(grades_list[0]) * 0.30 + float(grades_list[1]) * 0.60 + float(grades_list[2]) * 0.10

    if 88 <= ort <= 100:
        return f'{full_name}: AA'
    elif 80 <= ort <= 87:
        return f'{full_name}: BA'
    elif 73 <= ort <= 79:
        return f'{full_name}: BB'
    elif 66 <= ort <= 72:
        return f'{full_name}: CB'
    elif 60 <= ort <= 65:
        return f'{full_name}: CC'
    elif 55 <= ort <= 59:
        return f'{full_name}: DC'
    elif 50 <= ort <= 54:
        return f'{full_name}: DD'
    else:
        return f'{full_name}: FF'


def read_exam_grades() -> list:
    lst = []

    with open(file='exam_grades.txt', mode='r', encoding='utf-8') as file:
        for row in file:
            grade = exam_calculator(row)
            lst.append(grade)
    return lst


def register_grades(grade_list: list) -> None:
    with open(file='exam_grades.txt', mode='w', encoding='utf-8') as file:
        for i in grade_list:
            file.write(i + "\n")


def read_result() -> None:
    with open(file='exam_grades.txt', mode='r', encoding='utf-8') as file:
        for row in file:
            print(row)


def menu():
    print(f"""
    Menu
    ===========================
    Read Grades     --> 1
    Enter Grades    --> 2
    Register Grades --> 3
    Read Result     --> 4
    """)


def main():

    menu()

    while True:

        process = input('Please enter the process you wish to do. ')
        match process:
            case '1':
                read_exam_grades()
                print('Grades has been readed...! ')

            case '2':
                taking_data_from_student(input('First Name: '),
                                         input('Last Name: '),
                                         float(input('Midterm result: ')),
                                         float(input('Final result: ')),
                                         float(input('Homework point: ')))

            case '3':
                result = read_exam_grades()
                register_grades(result)

            case '4':
                read_result()
            case _:
                print('Please choose valid process...! ')


main()
