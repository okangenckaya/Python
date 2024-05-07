
users_dic = {
    '1': {
        'user name': 'new',
        'password': '987',
    },
    '2': {
        'user name': 'old',
        'password': '578',
    },
    '3': {
        'user name': 'old.123',
        'password': '445',
    }
}

def get_user_data(users_dic: dict) -> list:
    user_data = []
    for i in users_dic:
        user_data.append(users_dic.get(str(i)).get('user name'))
    return user_data

def sign_up(user_name: str, password: str) -> dict:
    if user_name in get_user_data(users_dic):
        print('The user name you have typed is already taken. Please type another user name..! ')
    else:
        print('Your account has been created..! ')
        users_dic[str(len(users_dic)+1 )] = {
            'user name': user_name,
            'password': password,
        }

def sign_in(user_name: str, password: str) -> None:
    is_user_valid = False
    for i in range(1, len(users_dic) + 1):
        if users_dic.get(str(i)).get('user name') == user_name and users_dic.get(str(i)).get('password') == password:
            is_user_valid = True
            break
    if is_user_valid:
        print(f'Welcome {user_name}..!')
    else:
        print('Please check your details..!')

def main():
    while True:
        process = input('Enter your process: ').lower()
        match process:
            case 'exit':
                print('Application is closing..!')
                break
            case 'sign up':
                user_name = input('User Name: ')
                password = input('Password: ')
                sign_up(user_name, password)
                print(users_dic)
            case 'log in':
                user_name = input('User Name: ')
                password = input('Password: ')
                sign_in(user_name, password)
            case _:
                print('Please choose correct process..!')
main()
