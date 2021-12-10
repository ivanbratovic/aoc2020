import numpy as np


def seat_layout_from_file(filepath: str):
    """
    Reads input from a given file and returns the seat layout as a
    numpy 2D array (ndarray).
    """
    with open(filepath, "r") as file:
        seats = [[c for c in line.strip()] for line in file.readlines()]
    return np.array(seats)


def count_los(board: np.array, coords: tuple):
    """
    Counts occupied seats in eight directions following a
    straight line.
    """
    row, col = coords
    occupied = 0
    neighbours = np.zeros((3,3))    # For keeping of seats hit in the 8 directions
    neighbours[1][1] = 1
    distance = 1
    while np.any(neighbours == 0):
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                if dx == 0 and dy == 0:
                    continue
                x = row + distance*dx
                y = col + distance*dy
                if 0 <= x < board.shape[0] and 0 <= y < board.shape[1]:
                    if neighbours[dx+1][dy+1] == 0:
                        if board[x][y] == "L":
                            neighbours[dx+1][dy+1] = 1
                        elif board[x][y] == "#":
                            occupied += 1
                            neighbours[dx+1][dy+1] = 1
                else:
                    neighbours[dx+1][dy+1] = 1
        distance += 1

    return occupied


def count_adjacent(board: np.array, coords: tuple):
    """
    Count occupied seats in the eight seats surrounding
    the seat given by coords.
    """
    row, col = coords
    occupied = 0
    if board[coords] == ".":
        return (-1,-1)
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if dx == 0 and dy == 0:
                continue
            x = row + dx
            y = col + dy
            if 0 <= x < board.shape[0] and 0 <= y < board.shape[1]:
                if board[x][y] == "#":
                    occupied += 1
    return occupied


def iter_board(board: np.array, limit: int, counter):
    changing = True
    while changing:
        changing = False
        new_board = np.empty_like(board)
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                occupied = counter(board,(i,j))
                if cell == "L" and occupied == 0:
                    new_board[i][j] = "#"
                    changing = True
                elif cell == "#" and occupied >= limit:
                    new_board[i][j] = "L"
                    changing = True
                else:
                    new_board[i][j] = cell
        board = new_board
    return board


def main(file: str):
    """
    Main function. Contains top-level logic.
    """
    seats =  seat_layout_from_file(file)
    # Part 1 - counting adjacent neighbours
    final_iter = iter_board(seats, 4, lambda x,y: count_adjacent(x,y))
    counts = dict(zip(*np.unique(final_iter, return_counts=True)))
    print("Part 1:", counts["#"])
    # Part 2 - with Line of Sight
    final_iter = iter_board(seats, 5, lambda x,y: count_los(x,y))
    counts = dict(zip(*np.unique(final_iter, return_counts=True)))
    print("Part 2:", counts["#"])

if __name__ == "__main__":
    print("-- TEST --")
    main("test.txt")
    print("-- REAL --")
    main("input.txt")

