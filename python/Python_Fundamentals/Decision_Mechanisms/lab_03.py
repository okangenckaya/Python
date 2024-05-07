
# how to print months inside season taken by user ?

season = input('please enter a season name. ').lower()

if season == 'autumn':
    print('Months belonging to season you have entered is listed: September, October, and November. ')
elif season == 'fall':
    print('Months belonging to season you have entered is listed: September, October, and November. ')
elif season == 'winter':
    print('Months belonging to season you have entered is listed: December, January, and February. ')
elif season == 'spring':
    print('Months belonging to season you have entered is listed: March, April, and May. ')
elif season == 'summer':
    print('Months belonging to season you have entered is listed: June, July, and August . ')
else:
    print('There is no season detected. ')

