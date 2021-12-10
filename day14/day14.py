import numpy as np
import re
import itertools


def instructions_from_file(filepath: str):
    """
    Reads input from a given file and returns the list of
    instructions of form (address, value)
    """
    l = []
    with open(filepath, "r") as file:
        for line in file.readlines():
            line = line.strip().split(" = ")
            l.append([line[0]]+[line[1]])
    return l

def apply_mask_address(address: int, mask: str):
    mask_1 = [35-i for i in range(len(mask)) if mask[i] == "1"]
    mask_X = [35-i for i in range(len(mask)) if mask[i] == "X"]
    for i in range(36):
        mask = 1 << i
        if i in mask_X:
            address &= ~mask
        if i in mask_1:
            address |= mask
    addresses = []
    combinations = []
    for i in range(0,len(mask_X)+1):
        combinations += list(itertools.combinations(mask_X, i))
    for comb in combinations:
        new_address = address
        for bit in comb:
            mask = 1 << bit
            new_address |= mask
        addresses.append(new_address)
    return addresses

def apply_mask_value(value: int, mask: str):
    mask_0 = [35-i for i in range(len(mask)) if mask[i] == "0"]
    mask_1 = [35-i for i in range(len(mask)) if mask[i] == "1"]
    for i in range(36):
        mask = 1 << i
        if i in mask_0:
            value &= ~mask
        if i in mask_1:
            value |= mask
    return value

def main(file: str):
    """
    Main function. Contains top-level logic.
    """
    instructions = instructions_from_file(file)
    # Part 1 - value masking
    memory = {}
    for ins in instructions:
        i, val = ins[0], ins[1]
        if i == "mask":
            mask = val
        else:
            address = int(re.split(r"(\[|\])", i)[2])
            memory[address] = apply_mask_value(int(val), mask)
            
    print("Part 1:", sum(memory.values()))
    # Part 2 - address masking
    memory = {}
    for ins in instructions:
        i, val = ins[0], ins[1]
        if i == "mask":
            mask = val
        else:
            address_init = int(re.split(r"(\[|\])", i)[2])
            val = int(val)
            addresses = apply_mask_address(address_init, mask)
            for address in addresses:
                memory[address] = val
    print("Part 2:", sum(memory.values()))

if __name__ == "__main__":
    print("-- TEST --")
    main("test.txt")
    print("-- REAL --")
    main("input.txt")

