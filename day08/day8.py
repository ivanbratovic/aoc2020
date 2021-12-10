import numpy as np
import sys
import re

def instructions_from_file(filepath : str):
    """
    Reads input from file and returns the instructions of the program
    represented as a list of tuples (opcode, offset), e.g. ('jmp', -3)
    """
    instructions = []
    with open(filepath, "r") as file:
        for line in file.readlines():
            line = line.strip().split()
            opcode, offset = line[0], int(line[1])
            instructions.append((opcode, offset))
    return instructions

def run_program(instructions : list, start : int = 0, acc : int = 0, ignore : int = -1):
    """
    Runs the given instructions one by one.

    Ignores the jump command if ignore index is given.

    Returns the final accumulator total, and whether
    the program ended up in an infinite loop or not.
    """
    visited = []
    curr_instr = start
    while curr_instr < len(instructions):
        if curr_instr in visited:
            return acc, True
        visited.append(curr_instr)
        opcode, offset = instructions[curr_instr]

        if opcode == "nop":
            curr_instr += 1
        elif opcode == "acc":
            acc += offset
            curr_instr += 1
        elif opcode == "jmp":
            if curr_instr == ignore:
                curr_instr += 1
            else:
                curr_instr += offset

    return acc, False

def main(file: str):
    """
    Main function. Contains primary logic.
    """
    instructions = instructions_from_file(file)
    # Part 1
    print("Part 1:", run_program(instructions)[0])
    # Part 2
    for ignore_ins in [idx for idx,ins in enumerate(instructions) if ins[0] == "jmp"]:
        acc, looped = run_program(instructions, ignore=ignore_ins)
        if not looped:
            break
    print("Part 2:", acc)

if __name__ == "__main__":
    print("-- TEST --")
    main("test.txt")
    print("-- REAL --")
    main("input.txt")

