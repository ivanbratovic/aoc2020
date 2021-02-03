import numpy as np
import re

def expr_from_file(filepath: str):
    """
    Reads input from a given file and returns the expressions without
    the spaces
    """
    with open(filepath, "r") as file:
        expr = [[c for c in line.strip() if c != " "] for line in file.readlines()]
    return expr

class Char:
    """
    Class which overrides the basic operators, letting
    Python handle the evaluation of the input.
    """
    def __init__(self, v):
        self.v = v

    def __sub__(self, o):
        return Char(self.v * o.v)

    def __add__(self, o):
        return Char(self.v + o.v)

    def __mul__(self, o):
        return Char(self.v + o.v)

def calculcate_total(expr: list, part1: bool):
    total = 0
    for line in expr:
        for i, char in enumerate(line):
            if char == "*":
                line[i] = "-"
            if char == "+" and not part1:
                line[i] = "*"
            if re.match(r"[0-9]+", char):
                line[i] = "Char(" + char + ")"
        total += eval("".join(line)).v
    return total

def main():
    """
    Main function. Contains top-level logic.
    """
    expr = expr_from_file("input.txt")
    # Part 1 - mul=add
    print(calculcate_total(expr, True))
    # Part 2 - add>mul
    print(calculcate_total(expr, False))

main()
