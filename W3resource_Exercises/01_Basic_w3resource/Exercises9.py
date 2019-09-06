#Find max value of two members
def max_two(a, b):
	if a > b: return a
	else: return b

#Find max value of four members
def max_four(a, b, c, d):
	m1 = max_two(a, b)
	m2 = max_two(c, d)
	return max_two(m1, m2)

#Find min value of two members
def min_two(a, b):
	if a < b: return a
	else: return b

#Find min value of four members
def min_four(a, b, c, d):
	m1 = min_two(a, b)
	m2 = min_two(c, d)
	return min_two(m1, m2)

#main

print("Enter into four any integer numbers")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))
print("\nMax = "+ str(max_four(a, b, c, d)))
print("Min = "+ str(min_four(a, b, c, d)))