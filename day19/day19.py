import numpy as np
import re

rules = {}

def words_from_file(filepath: str):
    """
    Reads input from a given file and returns the words,
    while filling up the rules at the same time.

    Rules are a global variable so I don't have to pass it
    around in recursive calls later on.
    """
    global rules
    switch = 0
    words = []
    with open(filepath, "r") as file:
        for line in file.readlines():
            if line == "\n":
                switch = 1
                continue
            if switch == 0:
                line = line.strip().split(": ")
                rules[line[0]] = line[1]
            else:
                words.append(line.strip())
    return words

def get_regex(rulenum: str, p2: bool=False):
    """
    Recursivelly gets the rule of a given name/number.

    For part2, manually escape infinite loops with
    hardcoded escapes.

    """

    if p2:
        # just manually remove the loops
        if rulenum == "8":
            return get_regex("42", p2) + "+"
        elif rulenum == "11":
            a = get_regex("42", p2)
            b = get_regex("31", p2)
            return "(?:" + "|".join(f"{a}{{{n}}}{b}{{{n}}}" for n in range(1, 100)) + ")"

    rule = rules[rulenum]
    if re.fullmatch(r"\".\"", rule):
        return rule[1]
    else:
        parts = rule.split(" | ")
        res = []
        for part in parts:
            nums = part.split(" ")
            res.append("".join(get_regex(num, p2) for num in nums))
        return "(?:" + "|".join(res) + ")"

def main(file: str):
    """
    Main function. Contains top-level logic.
    """
    words = words_from_file(file)
    rule_1 = get_regex("0")
    rule_2 = get_regex("0", True)
    # Part 1 and 2
    s1 = 0
    s2 = 0
    for word in words:
        if re.fullmatch(rule_1, word):
            s1 += 1
        if re.fullmatch(rule_2, word):
            s2 += 1
    print("Part 1:", s1)
    print("Part 2:", s2)

if __name__ == "__main__":
    print("-- TEST --")
    main("test.txt")
    print("-- REAL --")
    main("input.txt")

