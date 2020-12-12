no_of_lines = 1000
count = 0
for i in range(no_of_lines):
    line = input()
    line = line.split()

    # 1-10, s:, wowesdfsdf
    limits = line[0].split('-')
    low = int(limits[0])
    high = int(limits[1])
    letter = line[1][0]
    word = line[2]
    tmp = 0
    # part 1

    # count letter occurences
    # for l in word:
    # 	if l == letter:
    # 		tmp += 1
    # if tmp >= low and tmp <= high:
    # 	count +=1

    # part 2
    if word[low-1] == letter:
        tmp += 1
    if word[high-1] == letter:
        tmp += 1
    if tmp == 1:
        count += 1
print ("# of valid passwords: ")
print (count)



