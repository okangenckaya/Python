
# Learn book quantity from the user. Then, try to find how much discount they earn and reduced price.
# one book equals 5 unit of currency.
# less than 20 books => 5% discount
# Between 21 and 50 books => 10% discount
# Between 51 and 75 books => 15% discount
# Between 76 and 100 books=> 25% discount
# a reminder..! Users cannot buy more than 100 books.


reminder = 'A reminder..! You cannot buy books more than 100'
print(reminder)

book_quantity = int(input('Please enter book quantity you bought. '))

if book_quantity <= 20:
    discount = 0.05
elif 21 <= book_quantity <= 50:
    discount = 0.10
elif 51 <= book_quantity <= 75:
    discount = 0.15
elif 76 <= book_quantity <= 100:
    discount = 0.25
else:
    discount = 0

reduced_price = (book_quantity * 5) - (book_quantity * 5 * discount)

if book_quantity <= 20:
    print(f'Congratulations! you have earned {discount * 100}% discount and reduced price you have to pay is {reduced_price}')
elif 21 <= book_quantity <= 50:
    print(f'Congratulations! you have earned {discount * 100}% discount and reduced price you have to pay is {reduced_price}')
elif 51 <= book_quantity <= 75:
    print(f'Congratulations! you have earned {discount * 100}% discount and reduced price you have to pay is {reduced_price}')
elif 76 <= book_quantity <= 100:
    print(f'Congratulations! you have earned {discount * 100}% discount and reduced price you have to pay is {reduced_price}')
else:
    print('You are not allowed to buy more than 100 books. ')

