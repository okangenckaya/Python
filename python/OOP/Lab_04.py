class Software_Developer:

    knowledge_language = []

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def software_language_str_to_list(self, software_language: str) -> list:
        return software_language.split(',')

    def append_list(self, language_list: list) -> None:
        for language in language_list:
            self.knowledge_language.append(language.lstrip())

    def show_profile(self):
        return (f'First Name: {self.first_name}\n'
                f'Last Name: {self.last_name}\n'
                f'Programming Language: {self.knowledge_language}\n')


def main():

    print(f'Menu\n'
          f'Type personnel information    ==> 1\n'
          f'Read personnel information    ==> 2\n'
          f'Add programming language      ==> 3\n'
          f'Exit                          ==> e\n')

    while True:
        process = input('Choose your process: ').lower()

        match process:
            case '1':
                personnel_data = Software_Developer(first_name=(input('First Name: ')), last_name=(input('Last Name: ')))
                print('Personnel has been added successfully...!')
            case '2':
                print(personnel_data.show_profile())
            case 'e':
                print('Application has been closed...!')
                break
            case '3':
                language = input('Please type into programming language: ')
                converting = personnel_data.software_language_str_to_list(language)
                personnel_data.append_list(converting)
                print(personnel_data.show_profile())
            case _:
                print('Please choose valid process...!')


main()

