def get_stdin_lines():
    num_lines = int(input())
    return [input() for i in range(num_lines)]
    

def main():
    lines = list(map(int,get_stdin_lines()))
    print(lines)
    # Ye olde triple for-loop
    for i, line_i in enumerate(lines):
        for j, line_j in enumerate(lines):
            for k, line_k in enumerate(lines):
                if i >= j:
                    continue
                if j >= k:
                    continue
                if line_i+line_j+line_k == 2020:
                    print(line_i*line_j*line_k)
    


main()