import itertools

PREAMBLE_LEN = 25

def ports_from_file(filepath : str):
    """
    Reads input from file and returns the list of XMAS
    ports as a list of numbers 
    """
    ports = []
    with open(filepath, "r") as file:
        [ports.append(int(line)) for line in file.readlines()]
    return ports


def main():
    """
    Main function. Contains primary logic.
    """
    ports = ports_from_file("input.txt")
    # Part 1
    for i, n in enumerate(ports):
        # Just skip the preamble
        if i < PREAMBLE_LEN:
            continue
        candidates = ports[i - PREAMBLE_LEN:i]
        # Check if current number is sum of any
        # two out of PREAMBLE_LEN previous ports
        if n not in [x + y for x,y in itertools.combinations(candidates, 2)]:
            invalid = n
            break
    print(invalid)
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
    print(solution)

main()
    