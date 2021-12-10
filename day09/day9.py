import itertools

def ports_from_file(filepath : str):
    """
    Reads input from file and returns the list of XMAS
    ports as a list of numbers 
    """
    with open(filepath, "r") as file:
        return [int(line) for line in file.readlines()]


def main(file: str, preamble_len: int):
    """
    Main function. Contains primary logic.
    """
    ports = ports_from_file(file)
    # Part 1
    invalid = -1
    for i, n in enumerate(ports):
        # Just skip the preamble
        if i < preamble_len:
            continue
        candidates = ports[i - preamble_len:i]
        # Check if current number is sum of any
        # two out of PREAMBLE_LEN previous ports
        if n not in [x + y for x,y in itertools.combinations(candidates, 2)]:
            invalid = n
            break
    print("Part 1:", invalid)
    # Part 2
    # Check all possible ranges for the invalid number
    solution = 0
    for idx_low in range(len(ports) - 1):
        for idx_high in range(idx_low + 1, len(ports)):
            r = ports[idx_low:idx_high + 1]
            s = sum(r)
            if s == invalid:
                solution = min(r) + max(r)
                break
            if s > invalid:
                # Move on to next low index because the sum can't decrease
                break
        if solution > 0:
            # We found the task solution
            break
    print("Part 2:", solution)

if __name__ == "__main__":
    print("-- TEST --")
    main("test.txt", 5)
    print("-- REAL --")
    main("input.txt", 25)

    