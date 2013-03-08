import sys

sum = 0
n = 0

#Sum imput values
file_name = 'data2.txt'
for num in open(file_name):
	sum += float(num)
	n += 1

# Added comment - CU

print sum/n
