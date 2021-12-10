import numpy as np
import sys
import re

def map_from_file(filepath : str):
    """
    Reads input and returns a numpy.ndarray
    representing the main map data.
    """
    list_lines = []
    with open(filepath, "r") as file:
        lines = file.readlines()
        for line in lines:
            l = []
            for char in line.strip():
                l.append(char)
            list_lines.append(l)
    return np.array(list_lines)

def map_move(coords : np.array, map : np.ndarray, move : np.array):
    """
    Moves the coordinates according to the move,
    and returns the location (. or #) of the new
    coordinates using the map.
    """
    coords += move
    coords[1] = coords[1] % map.shape[1]
    if (coords[0] >= (map.shape[0])):
        return coords, None
    return coords, map[tuple(coords.tolist())]

def main(file: str):
    """
    Main function. Contains primary logic.
    """
    area_map =  map_from_file(file)
    moves = list(map(np.array, [[1,1],[1,3],[1,5],[1,7],[2,1]]))
    
    product = 1
    for move in moves:
        location = area_map[0,0]
        coords = np.array([0,0])
        trees = 0

        while location is not None:
            # Execute moves until you can't anymore
            if location == "#":
                trees += 1
            coords, location = map_move(coords, area_map, move)
        if move is moves[1]:
            print("Part 1:", trees)

        product *= trees
        
    print("Part 2:", product)

if __name__ == "__main__":
    print("-- TEST --")
    main("test.txt")
    print("-- REAL --")
    main("input.txt")

