
#Below 18.9 kg/m2 = Underweight

#19 - 24.9 kg/m2 = Healthy Weight

#25 - 29.9 kg/m2 = Overweight

#30 - 34.9 kg/m2 = Obesity

#35 ve üzeri olanlar = Extreme obesity


kilo = float(input('Enter your lenght . '))
boy = float(input('Enter your weight. '))

bmi = kilo / (boy / 100)**2

if bmi <= 18.9:
    print('Result: Underweight')
elif 19 <= bmi <= 24.9:
    print('Result: Healthy Weight.')
elif 25 <= bmi <= 29.9:
    print('Result: Overweight.')
elif 30 <= bmi <= 34.9:
    print('Result: Obesity.')
else:
    print('Result: Extreme obesity.')

