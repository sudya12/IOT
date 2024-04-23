# Using for loop, write and run a Python program to find factorial from 0 to
10

import math
def func(a=0):
    print(f"factorial of {a} is: {math.factorial(a)}")
for i in range(11):
    func(i)