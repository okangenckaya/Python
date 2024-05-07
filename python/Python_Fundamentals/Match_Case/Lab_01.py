

a_reminder = "A Reminder: Please type hemisphere which you live in as 'north' or 'south'..!"
print(a_reminder)

hemisphere = input('Please enter hemisphere where you live. ').lower()
season = input('Please type a season name. ').lower()

if hemisphere == 'north':
    match season:
        case 'winter':
            print('December, January, February. ')
        case 'spring':
            print('March, April, May. ')
        case 'summer':
            print('June, July, August. ')
        case 'autumn':
            print('September, October, November. ')
        case 'fall':
            print('September, October, November. ')
        case _:
            print('Please type a correct season name. ')
elif hemisphere == 'south':
    match season:
        case 'winter':
            print('June, July, August. ')
        case 'spring':
            print('September, October, November. ')
        case 'summer':
            print('December, January, February. ')
        case 'autumn':
            print('March, April, May. ')
        case 'fall':
            print('March, April, May. ')
        case _:
            print('Please type a correct season name. ')
else:
    print('Invalid hemisphere name..! ')