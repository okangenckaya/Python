#Nested If-Else

velocity = float(input('Enter the velocity. '))
vehicle = input('Enter your vehicle type. ').lower()


if velocity > 0:
    if vehicle == 'car':
        if velocity <= 90:
            print("You haven't exceeded the speed limit.")
        else:
            print('You have exceeded the speed limit.')
    if vehicle == 'truck':
        if velocity <= 60:
            print("You haven't exceeded the speed limit.")
        else:
            print('You have exceeded the speed limit.')

    if vehicle == 'Motocycle':
        if velocity <= 90:
            print("You haven't exceeded the speed limit.")
        else:
            print('You have exceeded the speed limit.')

    else:
        print('Please enter valid vehicle type. ')
else:
    print('Pleae enter valid velocity limit. ')






