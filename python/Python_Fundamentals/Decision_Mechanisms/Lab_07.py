
# How to print letter grade by calculating average point when mid-term point, final point, and homework point taken by the user ?

midd_term_point = float(input('Please type your mid-term exam result. '))
final_point = float(input('Please type your final exam result . '))
in_class_assignment_point = float(input('Please type your homework result. '))

point = midd_term_point * 0.30 + final_point*0.60 + in_class_assignment_point * 0.10

if point > 100:
    print('Please type valid points .')
if 85 <= point <= 100:
    print('Letter grade: AA.')
elif 75 <= point <= 84:
    print('Letter grade: BA.')
elif 65 <= point <= 74:
    print('Letter grade: BB.')
elif 55 <= point <= 64:
    print('Letter grade: CB.')
elif 50 <= point <= 54:
    print('Letter grade: CC.')
elif 45 <= point <= 49:
    print('Letter grade: DC.')
elif 36 <= point <= 44:
    print('Letter grade: DD.')
elif 0 <= point <= 35:
    print('Letter grade: FF.')
else:
    print('Please type valid points.')

