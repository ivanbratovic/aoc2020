import numpy as np
import itertools

def ratings_from_file(filepath : str):
    """
    Reads input from file and returns the list of
    joltage ratings as a list of numbers 
    """
    with open(filepath, "r") as file:
        joltages = [int(line) for line in file.readlines()]
    return sorted(joltages)

def reduce_combinations(joltages : list):
    """
    Returns a dictionary containing the possible
    permutations counts
    """
    accumulator = {0: 1} # hehe pun intended

    joltages.append(joltages[-1] + 3)

    for joltage in joltages:
        accumulator[joltage] = 0
        if joltage - 3 in accumulator:
            accumulator[joltage] += accumulator[joltage - 3]
        if joltage - 2 in accumulator:
            accumulator[joltage] += accumulator[joltage - 2]
        if joltage - 1 in accumulator:
            accumulator[joltage] += accumulator[joltage - 1]
    
    return accumulator[joltages[-1]]

def main():
    """
    Main function. Contains top-level logic.
    """
    joltage =  ratings_from_file("input.txt")
    # Part 1
    diff = np.diff([0] + joltage + [max(joltage)+3])
    counts = dict(zip(*np.unique(diff, return_counts=True)))
    print(counts[1] * counts[3])
    # Part 2
    print(reduce_combinations(joltage))


main()
