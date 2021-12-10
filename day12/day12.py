import numpy as np


def instructions_from_file(filepath: str):
    """
    Reads input from a given file and returns the seat layout as a
    numpy 2D array (ndarray).
    """
    with open(filepath, "r") as file:
        instructions = [(line[0], int(line[1:]))  for line in file.readlines()]
    return instructions

def go_direction(coords: tuple, direction: str, amount: int):
    x, y = coords
    if direction == "N":
        y += amount
    elif direction == "S":
        y -= amount
    elif direction == "E":
        x += amount
    elif direction == "W":
        x -= amount
    return x, y

def run_ship(instructions: list):
    x, y = 0, 0
    dirs = ["N", "E", "S", "W"]
    facing = "E"
    for instruction in instructions:
        direction, amount = instruction
        x, y = go_direction((x,y), direction, amount)    # Move N, E, S, W
        if direction == "F":
            x,y = go_direction((x,y), facing, amount)
        if direction == "L":
            # L rotation is inverted R rotation
            amount = -amount
            direction = "R" 
        if direction == "R":
            facing = dirs[(dirs.index(facing)+(amount//90))%4]

    print("Part 1:", abs(x)+abs(y))

def run_with_waypoint(instructions: list):
    ship_x, ship_y = 0, 0
    way_x, way_y = 10, 1
    for rule in instructions:
        direction, amount = rule
        way_x,way_y = go_direction((way_x,way_y), direction, amount)
        if direction == "F":
            ship_x += way_x * amount
            ship_y += way_y * amount
        if amount == 180 and (direction == "R" or direction == "L"):
            way_x, way_y = -way_x, -way_y
        elif direction == "L":
            way_x, way_y = -way_x, -way_y
            direction = "R"

        if direction == "R":
            if amount == 90:
                way_x, way_y = way_y, -way_x
            if amount == 270:
                way_x, way_y = -way_y, way_x


    print("Part 2:", abs(ship_x) + abs(ship_y))

def main(file: str):
    """
    Main function. Contains top-level logic.
    """
    instructions = instructions_from_file(file)
    # Part 1
    run_ship(instructions)
    # Part 2 - with Waypoint
    run_with_waypoint(instructions)

if __name__ == "__main__":
    print("-- TEST --")
    main("test.txt")
    print("-- REAL --")
    main("input.txt")

