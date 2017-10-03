import re

f = open("regex_actual.txt")
num_list = []
for x in f:
	l = x.strip()
	if re.findall("[0-9]+", l):
		numbers = re.findall("([0-9]+)", l)
		for y in numbers:
			num_list.append(int(y))
print (sum(num_list))
		
