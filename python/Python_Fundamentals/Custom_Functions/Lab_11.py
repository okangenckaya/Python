

users = ['Taylor Alison Swift', 'Ariana Grande', 'Lady Gaga', 'Katy Perry', 'Jennifer Lopez',
         'Rihanna']


def mail_creating(users: list) -> list:
    user_lst = []
    for user in users:
        divided_full_name = user.lower().split(' ')
        if len(divided_full_name) > 1:
            first_name = divided_full_name[0]
            last_name = divided_full_name[-1]
        user_lst.append(f'{first_name}.{last_name}@newadress.com')

    return user_lst


print(mail_creating(users))

