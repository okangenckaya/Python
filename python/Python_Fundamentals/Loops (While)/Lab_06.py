
# Take a year from the user and if this year is between 1920 and nowadays, give feedback that you have found or not found.

from datetime import datetime

started_year = 1920

searching_year = int(input('Please enter a year you are looking for. '))

is_exist = False

while started_year <= datetime.now().year:
    if started_year == searching_year:
        print(f'The year has been found. The year looking for is {searching_year}. ')
        is_exist = True
        break

    started_year += 1

if not is_exist:
    print(f'the year has not been found. ')



