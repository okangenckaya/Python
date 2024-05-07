#Decoration

from math import pow, factorial
from time import sleep, time


def calculate_execution_time(func):
    def inner_func(*args, **kwargs):
        start_process = time()
        sleep(2)
        func(*args, **kwargs)
        end_process = time()
        print(f'==================\n'
              f'Start Time: {start_process}\n'
              f'End: {end_process}\n'
              f'===================')

    return inner_func


@calculate_execution_time
def exponentiate(a: int, b: int):
    print(f'Result: {pow(a, b)}')


@calculate_execution_time
def calculating_factorial(number: int):
    print(f'Result: {factorial(number)}')


@calculate_execution_time
def sum_numbers(x: int, y: int, z: int):
    print(f'Result: {x + y + z}')


exponentiate(2, 3)
calculating_factorial(3)
sum_numbers(2, 3, 5)

