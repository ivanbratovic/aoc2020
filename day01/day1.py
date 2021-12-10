def lines_from_file(filepath: str):
    with open(filepath, "r") as file:
        return list(map(int, file.readlines()))

def main(file: str):
    lines = lines_from_file(file)
    #print(lines)
    # Ye olde triple for-loop
    part1 = False
    for i, line_i in enumerate(lines):
        for j, line_j in enumerate(lines):
            if not part1:
                if line_i+line_j == 2020:
                    part1 = True
                    print("Part 1:", line_i*line_j)
            for k, line_k in enumerate(lines):
                if i >= j:
                    continue
                if j >= k:
                    continue
                if line_i+line_j+line_k == 2020:
                    print("Part 2:", line_i*line_j*line_k)
    


if __name__ == "__main__":
    print("-- TEST --")
    main("test.txt")
    print("-- REAL --")
    main("input.txt")
