import sys

sum = 0
n = 0

#Sum imput values
for num in open('data2.txt'):
	sum += float(num)
	n += 1

# Added comment - CU

print sum/n
