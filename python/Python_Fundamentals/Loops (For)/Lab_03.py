
# Take beginning, finish, and step information from the user and calculate the numbers' square by these information.

b = int(input('Please enter the beginning value. '))
f = int(input('Please enter the final value. '))
s = int(input('Please enter the step value. '))


for i in range(b, f+1, s):
    print(i ** 2)



