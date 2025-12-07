import numpy as np
with open("input_8.txt") as f:
	input = np.asarray(([[i for i in line] for line in f.read().split("\n")]))
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
	for i, coordinate in enumerate(antennas[antenna_type][:-1]):
		for second_coordinate in antennas[antenna_type][i+1:]:
			delta_i = second_coordinate[0] - coordinate[0]
			delta_j = second_coordinate[1] - coordinate[1]
			node_1 = (coordinate[0] - delta_i, coordinate[1] - delta_j)
			node_2 = (second_coordinate[0] + delta_i, second_coordinate[1] + delta_j)
			for node in [node_1, node_2]:
				if node[0] >= 0 and node[0] < N and node[1] >= 0 and node[1] < M:
					nodes.add(node)
print(len(nodes))