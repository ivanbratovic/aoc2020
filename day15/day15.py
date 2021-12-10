import numpy as np
import re
import itertools


def numbers_from_file(filepath: str):
    """
    Reads input from a given file and returns the list of all numbers
    spoken
    """
    with open(filepath, "r") as file:
        seats = [line.strip().split(",") for line in file.readlines()]
    return np.array(seats)

def before(l, i, num):
    for j in range(i, -1, -1):
        if l[j] == num:
            return j+1
    return 0

def second_before(l: list, i: int, num: int):
    visited = False
    for j in range(i, -1, -1):
        if not visited and l[j] == num:
            visited = True
            continue
        if visited and l[j] == num:
            return j+1
    return 0

def main(file: str):
    """
    Main function. Contains top-level logic.
    """
    l = numbers_from_file(file)[0]
    l = list(map(int, l))
    # Part 1 and 2
    # Part 2 is slow (takes about 30 seconds) but did the job
    i = -1
    before = {}
    second_before = {}
    for part, limit in enumerate([2020, 30000000]):
        while (i != limit):
            i += 1
            if i < len(l):
                new = l[i]
                before[new] = i
                continue
            last = new
            new = 0
            if last in before and last not in second_before:
                new = 0
            else:
                new = before[last] - second_before[last]
            if new not in before:
                before[new] = i
            else:
                second_before[new] = before[new]
                before[new] = i
        print(f"Part {part+1}: {last}")


if __name__ == "__main__":
    print("-- TEST --")
    main("test.txt")
    print("-- REAL --")
    main("input.txt")

