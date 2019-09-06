def sum_three(a, b, c):
	sum_ = (a + b +c)
	if a == b == c :
		sum_ = sum_*3
	return sum_

a = int(input("Enter into number 1 = "))
b = int(input("Enter into number 2 = "))
c = int(input("Enter into number 3 = "))

print("Sum of three numbers is : "+str(sum_three(a, b, c)))