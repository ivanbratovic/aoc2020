import numpy as np
import sys
import re

def bag_rules_from_file(filepath : str):
    """
    Reads input from file and returns the rules of bag
    placement represented as a dictionary
    """
    rules = {}
    # Get the bag names and counts only
    with open(filepath, "r") as file:
        for line in file.readlines():
            line = re.split(r"( bags contain | bags*, | bags*\.)", line.strip())
            top_bag = line[0]
            inside_bags = line[2:-1:2]
            # Build a dictionary
            # - Key: bag name (e.g. 'light blue')
            # - Value: bag name + count (e.g. ('dim crimson', 3))
            rules.setdefault(top_bag, [])
            for bag in inside_bags:
                if bag == "no other":
                    break
                rules[top_bag].append((bag[2:], int(bag[0])))
    return rules

def can_contain_gold(top : str, d : dict):
    """
    Checks recursively whether a given top bag can
    eventually contain a shiny gold bag.
    """
    for link in d[top]:
        if link[0] == "shiny gold" or can_contain_gold(link[0], d):
            return True
    return False

def count_bags_within(bag : str, d : dict):
    """
    Counts the total amount of possible bags within
    a given bag
    """
    uncounted = [(bag, 1)]
    count = 0

    while len(uncounted) != 0:
        bag, n = uncounted.pop()
        for inside in d[bag]:
            count += inside[1] * n
            uncounted.append((inside[0], inside[1]*n))
    return count



def main(file: str):
    """
    Main function. Contains primary logic.
    """
    rules =  bag_rules_from_file(file)
    # Part 1
    print("Part 1:", sum([1 if can_contain_gold(k, rules) else 0 for k in rules]))
    # Part 2
    print("Part 2:", count_bags_within("shiny gold", rules))


if __name__ == "__main__":
    print("-- TEST --")
    main("test.txt")
    print("-- REAL --")
    main("input.txt")

