import math

no_of_lines = 323
arr = []
rows = 323
cols =  31

for i in range (no_of_lines):
	line = input()
	arr.append(line)

r = 0
c = 0
right = [1,3,5,7,1]
down = [1,1,1,1,2]
count = [0]*len(right)

for i in range(0,len(right)):
	r = 0
	c = 0
	while r < rows-1:
		c = c+right[i]
		c = c%31
		r = r+down[i]
		if arr[r][c] == '#':
			count[i] += 1
print("{} {} {} {} {}".format(count[0], count[1],count[2],count[3],count[4]))
print("product of trees encountered {}".format(math.prod(count)))
