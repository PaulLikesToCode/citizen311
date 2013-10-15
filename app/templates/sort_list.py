print "Hello World"
list = [3,5,2,8,2,1]
for index in range(1,len(list)):
	print list
	value = list[index]
	i = index - i
	while i >= 0:
		if value < list[i]:
			list[i + 1] = list[i]
			print list
			list[i] = value
			i = i - 1
		else:
			break
print list
