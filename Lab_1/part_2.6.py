
import sys
import math

def do_stuff():
    if len(sys.argv) != 4:
        print("EX) python part_2.6 1 -3 2")
        return

    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])

    if a == 0:
        print("a cannot be 0.")
        return

    d = b**2 - 4*a*c

    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print(f"solutions are: {root1}, {root2}")
    elif d == 0:
        root = -b / (2*a)
        print(f"solution is: {root}")
    else:
        print("no real solutions.")

do_stuff()