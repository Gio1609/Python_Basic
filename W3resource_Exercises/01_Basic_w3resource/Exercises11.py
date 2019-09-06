import math

#Function check prime number
def check_prime(n):
	if n<2: 
		return False
	if n == 2: 
		return True
	for x in range(2, int(math.sqrt(n))):
		if(n%x == 0): return False
		else:
			return True

#main
n = int(input("Enter into integer number n = "))
arr = []
for x in range(2,100):
	if n>0:
		if check_prime(x) is True:
			arr.append(x)
			n-=1
	else: break
print(arr)