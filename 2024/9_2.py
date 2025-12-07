with open("input_9") as f:
	input = f.read()
#input = "12345"
#input = "233313312141413140201"
n = len(input)

filesys = []
for i in range(0,n-1,2):
	filesys.append([str(i//2)] *  int(input[i]))
	if input[i+1] != "0":
		filesys.append(["."] * int(input[i+1]))
filesys.append([str((n-1)//2)] * int(input[-1]))
#print(filesys)
just_files = [file for file in filesys if "." not in file]
#print(just_files)
files_sorted = filesys.copy()
for file in reversed(just_files):
	l = len(file)
	index = files_sorted.index(file)
	for i, block in enumerate(files_sorted[:index]):
		m = len(block)
		if "." in block and m >= l: #need block to fit file and be left of it
			files_sorted[index] = ["."] * l #replace file with dots
			files_sorted[i] = file #replace block with file
			if m > l: # if block is bigger than file, fill with dots
				files_sorted = files_sorted[:i+1] + [["."]] * (m - l) + files_sorted[i+1:]
			break
sorted_flattened = [i for file in files_sorted for i in file]
#print(sorted_flattened)
#print(filesys)
print(files_sorted)
c = 0
for i, car in enumerate(sorted_flattened):
	if car != ".":
		c += i * int(car)
print(c)
#111080585254 too low
#6463936709941 too high
