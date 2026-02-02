# This program calculates the real roots of a quadratic equation (ax^2 + bx + c = 0)
import sys
import math

def do_stuff():
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])

    d = b**2 - 4*a*c

    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print(f"The solutions are: {root1}, {root2}") # The error was the use of invalid quotation marks ‘ ’ in print statements
    elif d == 0:
        root = -b / (2*a)
        print(f"The solution is: {root}")
    else:
        print("There are no real solutions.")

do_stuff()