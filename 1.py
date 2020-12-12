no_of_lines = 200
lines = []
for i in range(no_of_lines):
    line =input()
    line = int(line)
    lines.append(line)
a = 0
b = 0
c = 0
for i in lines:
	for j in lines:
		for k in lines:
			if i+j+k == 2020:
				a = i
				b = j
				c = k
				break
print (a)
print (b)
print (c)

print(a+b+c)
print(a*b*c)