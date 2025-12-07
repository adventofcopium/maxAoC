import numpy as np
with open("input_6.txt") as f:
    input = np.asarray([[i for i in line] for line in f.read().split("\n")])
def solution_2(input):
        # find starting position:
    N = len(input)
    M = len(input[0])
    c = 0
    starting = np.where(input == "^")
    i0,j0 = int(starting[0][0]), int(starting[1][0])
    for a in range(N):
        for b in range(M):
            input_copy = input.copy()
            break_flag = False
            if input_copy[a][b] != "#" and (a,b) != (i0,j0):
                input_copy[a][b] = "#"
                i,j = i0,j0
                for _ in range(9000):
                    if i > 0:
                        if input_copy[i-1][j] == "#":
                            input_copy = np.rot90(input_copy)
                            i,j = N-j-1,i
                        else:
                            i -= 1
                    else:
                        break_flag = True
                        break
                if not break_flag:
                    c += 1
    print(c)
solution_2(input)