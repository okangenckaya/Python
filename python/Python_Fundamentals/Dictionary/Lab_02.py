

phones = [
    {'name': 'iPhone 14 Pro Max', 'price': 80000},
    {'name': 'Samsung Galaxy Fold 5', 'price': 68000},
    {'name': 'HUAWEI Mate X', 'price': 68000},
    {'name': 'Xiaomi 13', 'price': 68000}

]

# How to sum all phone prices ?

total = 0
for phone in phones:
    total += phone['price']
print(f'Sum of all phone prices: {total} ')

# How to call above 80000 TL phone price ?

for phone in phones:
    if phone["price"] >= 69000:
        print(f'Name : {phone.get("name")} - Price: {phone["price"]}')

