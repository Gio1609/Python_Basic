#Function parse N
def parse_N(n):
	arr = []
	while(n>0):
		mod = n%10
		arr.append(mod)
		n = n//10
	return arr

#main
n = int(input("Enter into integer number n = "))
arr = parse_N(n)


print(arr)
