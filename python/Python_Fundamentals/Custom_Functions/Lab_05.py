

def sum(n1: int, n2: int, n3: int) -> int:
    return n1 + n2 + n3

def square(a:int ) -> None:
    print(f'Result: {a ** 2 }')

def main():

    number_1 = int(input('Please enter one number: '))
    number_2 = int(input('Please enter one number: '))
    number_3 = int(input('Please enter one number: '))
    total = sum(number_1, number_2, number_3)
    result = square(total)

main()



