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

def main(file: str):
    """
    Main function. Contains primary logic.
    """
    boarding_passes =  boarding_passes_from_file(file)
    # Part 1
    print("Part 1:", max(boarding_passes))
    # Part 2
    for i in range(2**10-1):
        top_3 = i >> 7
        if top_3 == 7 or top_3 == 0:
            continue
        if i not in boarding_passes:
            print("Part 2: {0} ({0:010b})".format(i))

if __name__ == "__main__":
    print("-- REAL --")
    main("input.txt")

