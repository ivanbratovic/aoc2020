import numpy as np
from functools import reduce

def seat_layout_from_file(filepath: str):
    """
    Reads input from a given file and returns the seat layout as a
    numpy 2D array (ndarray).
    """
    with open(filepath, "r") as file:
        a = int(file.readline())
        l = file.readline().strip().split(",")
    return a, l

def get_factor(a, b):
    b0 = b
    xi, xj = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        xi, xj = xj - q * xi, xi
    if xj < 0:
        xj += b0
    return xj

def chinese_remainder_theorem(n, a):
    # Uses direct construction of the solution
    s = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        s += a_i * get_factor(p, n_i) * p
    return s % prod

def main(file: str):
    """
    Main function. Contains top-level logic.
    """
    a, l =  seat_layout_from_file(file)
    #print(a, l)
    # Part 1 - brute forced
    b = False
    for i in range(a, a+100):
        for j in l:
            if j == "x":
                continue
            j = int(j)
            if i % j == 0:
                print("Part 1:", (i-a)*j)
                b = True
                break
        if b:
            break
    # Part 2 - CRT
    buses_shifted = [(int(l[i])-(i%int(l[i]))) for i in range(len(l)) if l[i] != "x"]
    n = []
    a = []
    for i in range(0, len(l)):
        t = l[i]
        if t != "x":
            n.append(int(t))
            a.append(int(t)-i)
    print("Part 2:", chinese_remainder_theorem(n, a))
if __name__ == "__main__":
    print("-- TEST --")
    main("test.txt")
    print("-- REAL --")
    main("input.txt")

