
def reverse(data):
	s = str(data)
	return int(s[::-1]);

def isPolindrome(d):
	return reverse(d) == d

i = 0
j = int(input('input number:	'))
print('------------------------------------------')
print('original:	'+str(j))

while not isPolindrome(j):
	# iteration limit
	if i > 1000:
		break
	i = i + 1
	j = j + reverse(j)

if i < 1000:
	print('iterations:	'+str(i))
else:
	print("iterations:	 1000+")
print('output:		'+str(j))
i = 0
