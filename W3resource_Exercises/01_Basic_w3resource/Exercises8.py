import math

def equation_second(a, b, c):
	delta = b*b - (4*a*c)
	print(delta)
	if delta < 0:
		print("Equation not values true")
	elif delta == 0:
		print("Equation have values x = "+str(-b/(2*a)))
	else:
		print("Equation have values x1 = "+str((-b - math.sqrt(delta))/(2*a)))
		print("Equation have values x2 = "+str((-b + math.sqrt(delta))/(2*a)))

print("\nProgram solve equation order second\n")

a = int(input("a = "))
while a == 0:
	print("a can't equal 0! Enter again")
	a = int(input("a = "))

b = int(input("b = "))
c = int(input("c = "))

equation_second(a, b, c)
