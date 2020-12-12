arr = [-1]*1000
values = [-1]*1000
i=0

line_prev = ''
valid_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
count = 0

def checkValid(i):
	for j in range (0,len(arr[i])):
		if arr[i][j] == 'byr':
			if len(values[i][j]) != 4:
				return False
			if (int(values[i][j])<1920 or int(values[i][j])>2002):
				return False
		elif arr[i][j] == 'iyr':
			if len(values[i][j]) != 4:
				return False
			if (int(values[i][j])<2010 or int(values[i][j])>2020):
				return False
		elif arr[i][j] == 'eyr':
			if len(values[i][j]) != 4:
				return False
			if (int(values[i][j])<2020 or int(values[i][j])>2030):
				return False
		elif arr[i][j] == 'hgt':
			if values[i][j][-2] == 'c' and values[i][j][-1] == 'm' and len(values[i][j])==5:
				if int(values[i][j][0:3])<150 or int(values[i][j][0:3])>193:
					return False
			elif values[i][j][-2] == 'i' and values[i][j][-1] == 'n' and len(values[i][j])==4:
				if int(values[i][j][0:2])<59 or int(values[i][j][0:2])>76:
					return False
			else:
				return False
		elif arr[i][j] == 'hcl':
			if values[i][j][0] == '#' and len(values[i][j]) == 7:
				for k in range (1, 7):
					if not values[i][j][k].isalnum():
						return False
			else:
				return False
		elif arr[i][j] == 'ecl':
			valid_vals = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
			if values[i][j] not in valid_vals:
				return False
		elif arr[i][j] == 'pid':
			if len(values[i][j]) == 9 and values[i][j][0] == '0':
				for v in values[i][j]:
					if not v.isnumeric():
						return False
			else:
				return False
	return True

while True:
	line = input()
	# exit on 2 consecutive empty lines
	if line == '' and line_prev == '':
		break
	# new entry after blank line
	# check the validity of previous entry
	elif line == '':
		flag = 0
		for v in valid_list:
			if v not in arr[i]:
				flag = 1
				break
		if flag == 0:
			# print(arr[i])
			if checkValid(i):
				count += 1
		i += 1
	# add keys to the entry
	elif arr[i] == -1:
		arr[i] = []
		values[i] = []
		tokens = line.split()
		for j in tokens:
			tmp = j.split(':')
			arr[i].append(tmp[0])
			values[i].append(tmp[1])
	else:
		tokens = line.split()
		for j in tokens:
			tmp = j.split(':')
			arr[i].append(tmp[0])
			values[i].append(tmp[1])
	line_prev = line
print(count)