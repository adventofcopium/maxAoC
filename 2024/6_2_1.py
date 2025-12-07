import numpy as np
with open("input_6.txt") as f:
    input = np.asarray([[i for i in line] for line in f.read().split("\n")])
    
def check_loop(grid, a, b, starting_values):
        # put a # at position (a,b) and check if it leads to a loop'
        visited = np.zeros((len(grid),len(grid[0])))
        if grid[a][b] != "#" and (a,b) != starting_values:
            grid[a][b] = "#"
            i,j = starting_values
            while i > 0:
                grid[i][j] = "X"
                if grid[i-1][j] == "#":
                    if visited[i][j] == 1:
                        return True
                    else:
                    	visited[i][j] = 1
                        grid = np.rot90(grid)
                        i,j = len(grid)-j-1,i
                    	visited = np.rot90(visited)
                else:
                	i -= 1
            return False

def solution_2(input):
        # find starting position:
    N = len(input)
    M = len(input[0])
    c = 0
    starting = np.where(input == "^")
    i0,j0 = int(starting[0]), int(starting[1])
    
    for a in range(N):
        for b in range(M):
            input_copy = input.copy()
            if check_loop(input_copy, a, b, (i0,j0)):
            	c += 1      
    print(c)
solution_2(input)