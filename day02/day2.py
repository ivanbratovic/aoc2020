import numpy as np
import sys
import re

def file_splitlines(filepath : str):
    """
    Reads input and returns a list of tuples
    representing the main data.
    """
    list_lines = []
    with open(filepath, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = re.split("[\-: ]", line.strip())
            for i in range(2):
                line[i] = int(line[i])
            line.pop(3)
            list_lines.append(tuple(line))
    return list_lines

def valid_1(tpl : tuple):
    """
    Validity checker for part 1
    """
    minimum, maximum, letter, string = tpl
    count = string.count(letter)
    if count >= minimum and count <= maximum:
        return 1
    return 0

def valid_2(tpl : tuple):
    """
    Validity checker for part 2
    """
    pos1, pos2, letter, string = tpl
    c1 = string[pos1-1]
    c2 = string[pos2-1]
    if c1 == letter and c2 != c1 or c2 == letter and c1 != c2:
        return 1
    return 0

def main():
    """
    Main function. Contains primary logic.
    """
    s1, s2 = 0, 0
    for line in file_splitlines("input.txt"):
        print(line)
        s1 += valid_1(line)
        s2 += valid_2(line)
    print(s1)
    print(s2)

main()
