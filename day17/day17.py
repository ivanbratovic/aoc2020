import numpy as np


def instructions_from_file(filepath: str):
    """
    Reads input from a given file and returns set of
    only the active cubes
    """
    with open(filepath, "r") as file:
        seats = [[1 if c == "#" else 0 for c in line.strip()] for line in file.readlines()]
    cubes = np.zeros((8,8,8,8), dtype=np.bool_)
    cubes[:len(seats),:len(seats[0]),0,0] = np.array(seats)
    return locate_active(cubes)

def locate_active(cubes: np.ndarray):
    # Returns the set of only the active cube coordinates,
    # given a full cube
    active = set()
    for x in range(cubes.shape[0]):
        for y in range(cubes.shape[1]):
            for z in range(cubes.shape[2]):
                for w in range(cubes.shape[3]):
                    if cubes[x,y,z,w] == 1:
                        active.add((x,y,z,w))
    return active

def count_neighbours(active: set, x, y, z, w):
    count = 0
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            for dz in [-1,0,1]:
                for dw in [-1,0,1]:
                    if not (dx==0 and dy==0 and dz==0 and dw==0):
                        if (x+dx, y+dy, z+dz, w+dw) in active:
                            count += 1
    return count

def get_range(active, cindex: int, d4: bool=True):
    if not d4: # 4D switch
        return [0]
    cmin, cmax = 1000, -1000
    for coords in active:
        if cmin > coords[cindex]:
            cmin = coords[cindex]
        if cmax < coords[cindex]:
            cmax = coords[cindex]
    return range(cmin-1, cmax+2)

def simulate(active: set, num_iter: int, d4: bool):
    for it in range(num_iter):
        next_active = set()
        for x in get_range(active, 0):
            for y in get_range(active, 1):
                for z in get_range(active, 2):
                    # w coordinate range is only [0] if 4D isn't used 
                    # this way, the solution is generalized to 3D and 4D
                    for w in get_range(active, 3, d4):
                        nbr = count_neighbours(active, x, y, z, w)
                        # Conditions for (in)activity
                        if (x,y,z,w) not in active and nbr == 3:
                            next_active.add((x,y,z,w))
                        if (x,y,z,w) in active and nbr in [2,3]:
                            next_active.add((x,y,z,w))
        active = next_active
    print(len(active))

def main(file: str):
    """
    Main function. Contains top-level logic.
    """
    active = instructions_from_file(file)
    # Part 1 - 3D
    print("Part 1:", end=" ")
    simulate(active, 6, False)
    # Part 2 - with 4D
    print("Part 2:", end=" ")
    simulate(active, 6, True)

if __name__ == "__main__":
    print("-- TEST --")
    main("test.txt")
    print("-- REAL --")
    main("input.txt")

