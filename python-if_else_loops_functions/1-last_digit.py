#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number % 10
n2 = number % -10

if number < 0:
    n2 = number % -10
    print(f"Last digit of {number} is {n2} and is less than 6 and not 0")
elif n > 5:
    print(f"Last digit of {number} is {n} and is greater than 5")
elif n == 0:
    print(f"Last digit of {number} is {n} and is 0")
elif n < 6 and n != 0 and n > 0:
    print(f"Last digit of {number} is {n} and is less than 6 and not 0")
