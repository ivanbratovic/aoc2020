import numpy as np
from typing import List

def foods_from_file(filepath: str):
    """
    Reads input from a given file and returns the food list,
    and the allergens, as defined in https://adventofcode.com/2020/day/21.
    """
    foods = []
    with open(filepath, "r") as file:
        for line in file.readlines():
            line = line.strip().split("(")
            line[0] = line[0].strip().split()
            line[1] = line[1][9:-1].strip().split(", ")
            foods.append(line)
    return foods

def main(file: str):
    foodlist = foods_from_file(file)
    options = {}
    ingredient_count = {}
    # Figure out what ingredient could contain which allergen
    for food, allergens in foodlist:
        for ingredient in food:
            ingredient_count.setdefault(ingredient, 0)
            ingredient_count[ingredient] += 1
        for allergen in allergens:
            options.setdefault(allergen, set())
            possible = options[allergen]
            if len(possible) == 0:
                for ingredient in food:
                    possible.add(ingredient)
            else:
                possible_iter = list(possible)
                for possibility in possible_iter:
                    if possibility not in food:
                        possible.remove(possibility)
    all_allergenics = []
    for possibities in options.values():
        all_allergenics += possibities
    # Part 1
    print("Part 1:", sum([ingredient_count[ingredient] if ingredient not in all_allergenics else 0 for ingredient in ingredient_count]))
    # Part 2
    # Figure out exactly which allergen is in what ingredient
    allergens = {}
    while any([l != 0 for l in [len(possibility) for possibility in options.values()]]):
        for allergen, possibities in options.items():
            if len(possibities) == 1:
                allergens[allergen] = possibities.pop()
            else:
                for ingredient in allergens.values():
                    for remove_pos in options.values():
                        if ingredient in remove_pos:
                            remove_pos.remove(ingredient)

    print("Part 2:", ",".join(allergens[allergen] for allergen in sorted(allergens)))



if __name__ == "__main__":
    print("-- TEST --")
    main("test.txt")
    print("-- REAL --")
    main("input.txt")
