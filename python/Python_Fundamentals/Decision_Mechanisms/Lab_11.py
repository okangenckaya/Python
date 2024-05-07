
user_name = input('Please type your user name. ').lower()
password = input('Please type your password . ').lower()
role = input('Please type your role . ').lower()

if user_name == 'Team Leader':
    if password == '123':
        if role == 'admin':
            print('Welcome the major ..!')
        elif role == 'super admin':
            print('Welcome the beast..!')
        else:
            print('ou are unauthorized to access  ..!')
elif user_name == 'Master':
    if password == '321':
        if role  == 'manager':
            print('Welcome the manager..!')

        else:
            print('You are unauthorized to access .')
elif user_name == 'Trial Master':
    if password == '987':
        if role == 'manager':
            print('Welcome the raider..!')
        else:
            print('You are unauthorized to access .')
    else:
        print('Your password is invalid . ')
else:
    print('Your id is invalid . ')

