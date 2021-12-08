import numpy as np
import sys
import re

def boarding_passes_from_file(filepath : str):
    """
    Reads input and returns a list of all seat IDs
    """
    boarding_passes = []
    with open(filepath, "r") as file:
        for line in file.readlines():
            sid = 0
            for i, char in enumerate(line.strip()):
                if char == "B" or char == "R":
                    sid += 1 << (9-i)
            boarding_passes.append(sid)
    return boarding_passes

def main():
    """
    Main function. Contains primary logic.
    """
    boarding_passes =  boarding_passes_from_file("input.txt")
    # Part 1
    maximum = 0
    for i, boarding_pass in enumerate(boarding_passes):
        if boarding_pass > maximum:
            maximum = boarding_pass
    print(maximum)
    # Part 2
    for i in range(2**10-1):
        top_3 = i >> 7
        if top_3 == 7 or top_3 == 0:
            continue
        if i not in boarding_passes:
            print("{} ({:010b})".format(i,i))

main()
