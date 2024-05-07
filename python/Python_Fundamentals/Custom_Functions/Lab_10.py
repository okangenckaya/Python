

def creating_corporate_mail(full_name: str) -> str:
    divided_name = full_name.split(' ')
    name = divided_name[0]
    last_name = divided_name[-1]

    return f'{name}.{last_name}@xcorporation.com'


fullname_taken_by_user = input('Please type your name: ')
result = creating_corporate_mail(fullname_taken_by_user)
print(result)

