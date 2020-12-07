import numpy as np
import sys
import re

def bag_rules_from_file(filepath : str):
    """
    Reads input from file and returns the rules of bag
    placement represented as a dictionary
    """
    rules = {}
    lines = []
    # First get the bag names and counts only
    with open(filepath, "r") as file:
        for line in file.readlines():
            #line = line.strip().split(" bags contain ")
            line = re.split(r"( bags contain | bags*, |bags*\.)", line.strip())
            split = []
            for i in range(len(line)-1):
                if i % 2 == 0:
                    split.append(line[i])
            lines.append(split)
    # Then build a dictionary
    # - Key: bag name (e.g. light blue)
    # - Value: bag name + count (e.g. ('dim crimson', 3))
    for bags in lines:
        top_bag = bags[0].strip()
        rules.setdefault(top_bag, [])
        for bag in bags[1:]:
            if bag.strip() == "no other":
                break
            number, colour = int(bag[0]), bag[2:].strip()
            rules[top_bag].append((colour, number))
    return rules

def can_contain_gold(top : str, d : dict):
    """
    Checks recursively whether a given top bag can
    eventually contain a shiny gold bag.
    """
    for link in d[top]:
        if link[0] == "shiny gold":
            return True
        possible = can_contain_gold(link[0], d)
        if possible:
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
            inside = (inside[0], inside[1]*n)
            uncounted.append(inside)
    return count



def main():
    """
    Main function. Contains primary logic.
    """
    rules =  bag_rules_from_file("input.txt")
    # Part 1
    s = 0
    for k in rules.keys():
        if can_contain_gold(k, rules):
            s += 1
    print(s)
    # Part 2
    print(count_bags_within("shiny gold", rules))


main()
