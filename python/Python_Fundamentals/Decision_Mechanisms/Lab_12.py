
import random

number = random.randint(0, 50)


win = False
while win == False:

    taken_number = int(input('Please type a number: '))
    if taken_number < 0:
        print('Please type positive number...! ')
    else:
        if taken_number == number:
            print('Congratulations...! You have found it.')
            break
        elif number > taken_number:
            print("The number you have typed is below my number! Please type higher number. ")
        else:
            print("The number you have typed is above my number..! Please type lower number. ")

