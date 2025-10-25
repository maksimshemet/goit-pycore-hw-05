import re
from typing import Callable
from decimal import Decimal


def generator_numbers(text: str):

    numbers = re.findall(r'\d+\.\d+', text)

    for number in numbers:
        yield Decimal(number)

def sum_profit(text: str, func: Callable):
    total_income = 0

    for number in func(text):
        total_income += number

    return total_income


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")