import numpy as np
with open("input_6.txt") as f:
    input = np.asarray([[i for i in line] for line in f.read().split("\n")])
def solution_1(input):
    # find starting position:
    N = len(input)
    c = 0
    starting = np.where(input == "^")
    i,j = int(starting[0]), int(starting[1])
    input[i][j] == "X"
    while i > 0:
        if input[i-1][j] == "#":
            input = np.rot90(input)
            i,j = N-j-1,i
        else:
            if input[i][j] == ".":
                c += 1
                input[i][j] = "X"
            i -= 1
    print(c+2)
solution_1(input)