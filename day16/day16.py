import numpy as np
import sys, re

def tickets_from_file(filepath: str):
    """
    Reads input from a given file and returns the rules,
    my ticket, and other tickets
    """
    rules = {}
    ticket = []
    others = []
    switch = 0
    with open(filepath, "r") as file:
        for line in file.readlines():
            if line.strip() == "":
                switch += 1
                continue
            if switch == 0:
                rule = re.split(r"(: | or |-)", line.strip())
                rules[rule[0]] = [(int(rule[2]), int(rule[4])), (int(rule[6]), int(rule[8]))]
            elif switch == 1:
                if line.strip() == "your ticket:":
                    continue
                ticket = list(map(int, line.strip().split(",")))
            elif switch == 2:
                if line.strip() == "nearby tickets:":
                    continue
                others.append(list(map(int, line.strip().split(","))))

            
    return rules, ticket, others

def valid_value(val, rules):
    for rule in rules:
        for field in rules:
            for subset in rules[field]:
                if subset[0] <= val <= subset[1]:
                    return True
    return False

def main():
    """
    Main function. Contains top-level logic.
    """
    rules, ticket, others = tickets_from_file("input.txt")
    # Part 1
    s = 0
    for t in others:
        for val in t:
            if not valid_value(val, rules):
                s += val
    print(s)
    # Part 2
    # Get valid tickets
    valid = []
    for t in others:
        invalid = False
        for val in t:
            if not valid_value(val, rules):
                invalid = True
                break
        if not invalid:
            valid.append(t)
    valid = np.array(valid)
    possibilities = {}
    for i, col in enumerate(valid.transpose()):
        for field in rules:
            invalid = False
            for val in col:
                if not (rules[field][0][0] <= val <= rules[field][0][1])\
                and not(rules[field][1][0] <= val <= rules[field][1][1]):
                    invalid = True
                    break
            if not invalid:
                # Consider it only as a possibility, there might be more
                # positions which obey the rules
                possibilities.setdefault(i, []).append(field)

    # Narrow down fields by removing
    # only the ones we know are the only
    # option (only one possibility)
    prod = 1
    empty = False
    while not empty:
        empty = True
        for k in possibilities:
            candidates = possibilities[k]
            if len(candidates) == 0:
                continue
            empty = False
            if len(candidates) == 1:
                field = candidates[0]
                #print("{:2}: {}".format(k, field))
                # add ticket value to product (solution)
                if field[0:9] == "departure":
                    prod *= ticket[k]
                # remove field from all possibilities
                for k in possibilities:
                    if field in possibilities[k]:
                        possibilities[k].remove(field)
    print(prod)

main()
