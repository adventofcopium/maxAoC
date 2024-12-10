import numpy as np
with open("input_8.txt") as f:
	input = np.asarray([[i for i in line] for line in f.read().split("\n")])
#print(input)
antennas = {}
N = len(input)
M = len(input[0])
for i in range(N):
	for j in range(M):
		if input[i][j] != ".":
			if input[i][j] in antennas.keys():
				antennas[input[i][j]].append((i,j))
			else:
				antennas[input[i][j]] = [(i,j)]
#print(antennas)
nodes = set()
for antenna_type in antennas.keys():
	for i, (i_1, j_1) in enumerate(antennas[antenna_type][:-1]):
		for (i_2, j_2) in antennas[antenna_type][i+1:]:
			delta_i = i_2 - i_1
			delta_j = j_2 - j_1
			a,b = 0,0
			while (0 <= (i_1 - a * delta_i) < N) and (0 <= (j_1 - a * delta_j) < M):
				new_node = (i_1 - a * delta_i, j_1 - a * delta_j)
				nodes.add(new_node)
				a += 1
			while (0 <= (i_2 + b * delta_i) < N) and (0 <= (j_2 + b * delta_j) < M):
				new_node = (i_2 + b * delta_i, j_2 + b * delta_j)
				nodes.add(new_node)
				b += 1
print(len(nodes))