import numpy as np
import sys
import re

def voting_groups_from_file(filepath : str):
    """
    Reads input from file and returns two things:
     + Sets of group votes (with unique votes for the group) for part 1
     + All group votes by person for part 2
    """
    groups = []
    group_sets = []
    with open(filepath, "r") as file:
        group_set = set()
        answers = []
        for line in file.readlines():
            person = []
            if line.strip() == "":
                groups.append(answers)
                group_sets.append(group_set)
                group_set = set()
                answers = []
                continue
            for i, char in enumerate(line.strip()):
                person.append(char)
                group_set.add(char)
            answers.append(person)
        groups.append(answers)
        group_sets.append(group_set)
    return groups, group_sets

def main(file: str):
    """
    Main function. Contains primary logic.
    """
    groups, group_sets =  voting_groups_from_file(file)
    # Part 1
    print(sum([len(g) for g in group_sets]))
    # Part 2
    s = 0
    for group in groups:
        count = len(group)
        d = {}
        for person in group:
            for vote in person:
                d.setdefault(vote, 0)
                d[vote] += 1
        for k in d.keys():
            if d[k] == count:
                s+=1
    print(s)
    # Part 2

if __name__ == "__main__":
    print("-- TEST --")
    main("test.txt")
    print("-- REAL --")
    main("input.txt")

