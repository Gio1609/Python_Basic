#Function list divisors
def list_divisors(n):
	arr = []
	for x in range(1, n):
		if(n % x == 0):
			arr.append(x)
	return arr

#main
n = int(input("Enter into natural number n = "))
list_div = list_divisors(n)
print(str(n)+" have: "+str(len(list_div))+" divisors")
print("List divisors of "+str(n)+" is : "+ str(list_div))