from itertools import product
with open("input_7.txt") as f:
	input =f.read().split("\n")
results = [int(i) for i in [line.split(":")[0] for line in input]]
#print(results)
factors = []
for line in input:
	line = line.split(":")[1]
	factors.append([int(i) for i in line[1:].split(" ")])
#print(factors)
c = 0
for i, result in enumerate(results):
	terms = factors[i]
	perms = list(product(range(2), repeat = len(terms)-1))
	#print(perms)
	for perm in perms:
		d = terms[0] 
		for j, term in enumerate(terms[1:]):
			#print(perms[j])
			if perm[j] == 1:
				d *= term
			else:
				d += term
		#print(d)
		if d == result:
			c += result
			break
print(c)