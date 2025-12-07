with open("input_9.txt") as f:
	input = f.read()
#input = "12345"
#input = "2333133121414131402"
n = len(input)

filesys = []
for i in range(0,n-1,2):
	for _ in range(int(input[i])):
		filesys.append(str(i//2))
	for _ in range(int(input[i+1])):
		filesys.append(".")
for _ in range(int(input[-1])):
	filesys.append(str((n-1)//2))
#print(filesys)
just_files = [i for i in filesys if i != "."]
#print(just_files)
num_files = len(just_files)
files_sorted = []
for i in range(num_files):
	if filesys[i] != ".":
		files_sorted.append(filesys[i])
	else:
		files_sorted.append(just_files[-1])
		just_files = just_files[:-1]
print(files_sorted)
c = 0
for i, file in enumerate(files_sorted):
	c += i * int(file)
print(c)