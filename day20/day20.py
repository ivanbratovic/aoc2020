import numpy as np
from typing import List

def binary_invert(num: int):
    numbits = [1 if (num & (1 << bitpos)) else 0 for bitpos in range(10)]
    bits = "".join(["1" if bit != 0 else "0" for bit in numbits])
    return int(bits, 2)

class Tile:
    def __init__(self, id: int, rows: list):
        self.id = id
        self.parse_rows(rows)
        self.rows2cols()

    def rot90(self):
        """ Rotates tile 90 deg clockwise"""
        new_cols = []
        for row in self.rows[::-1]:
            new_cols.append(binary_invert(row))
        self.rows = self.cols
        self.cols = new_cols

    def test_rotation(self):
        # TEST for rotation
        rows_before = list(self.rows)
        cols_before = list(self.cols)
        self.rot90()
        assert not all([rows_before[i] == self.rows[i] for i in range(10)])
        assert not all([cols_before[i] == self.cols[i] for i in range(10)])
        self.rot90()
        assert not all([rows_before[i] == self.rows[i] for i in range(10)])
        assert not all([cols_before[i] == self.cols[i] for i in range(10)])
        self.rot90()
        assert not all([rows_before[i] == self.rows[i] for i in range(10)])
        assert not all([cols_before[i] == self.cols[i] for i in range(10)])
        self.rot90()
        assert all([rows_before[i] == self.rows[i] for i in range(10)])
        assert all([cols_before[i] == self.cols[i] for i in range(10)])

    def aligns(self, obj) -> int:
        assert isinstance(obj, Tile)

        if self is obj:
            return False

        for rot in range(4):
            obj.rot90()
            if self.rows[0] in (obj.rows[-1], obj.rows[0]):
                return True
            if self.rows[-1] in (obj.rows[0], obj.rows[-1]):
                return True
            if self.cols[0] in (obj.cols[-1], obj.cols[0]):
                return True
            if self.cols[-1] in (obj.cols[0], obj.cols[-1]):
                return True
        return False


    def parse_rows(self, rows: List[str]) -> None:
        self.rows = []
        for row in rows:
            rowval = int("".join(["1" if c == "#" else "0" for c in row ]), 2)
            self.rows.append(rowval)

    def rows2cols(self) -> List[int]:
        self.cols = []
        for bitpos in range(9, -1, -1):
            col = 0
            for row in range(10):
                bit = 1 if (self.rows[row] & (1 << bitpos) != 0) else 0
                col += bit << row
            self.cols.append(col)


def tiles_from_file(filepath: str):
    """
    Reads input from a given file and returns the tiles,
    as defined in https://adventofcode.com/2020/day/20.

    All tiles store 10-bit numbers that represent each
    column and each row.
    """
    tiles = []
    with open(filepath, "r") as file:
        tid : int = -1
        rows : List[str] = []
        for line in file.readlines():
            line = line.strip()
            if line == "":
                if tid != -1:
                    tiles.append(Tile(tid, rows))
                    rows = []
                    tid = -1
            elif line[0:4] == "Tile":
                tid = int(line[5:-1])
            else:
                rows.append(line)
    return tiles

def main(file: str):
    """
    Main function. Contains top-level logic.
    """
    tiles = tiles_from_file(file)

    # PART 1 - The whole pattern is not important
    # Find 4 tiles that don't match exactly 4 others

    corner_tiles = []
    for tile in tiles:
        aligned_tiles = sum([1 if tile.aligns(t) else 0 for t in tiles])
        if aligned_tiles == 2:
            corner_tiles.append(tile.id)
    #print(corner_tiles)
    print("Part 1:", np.prod(corner_tiles))


if __name__ == "__main__":
    print("-- TEST --")
    main("test.txt")
    print("-- REAL --")
    main("input.txt")
