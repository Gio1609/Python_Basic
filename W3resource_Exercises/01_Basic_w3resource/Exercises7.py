def equation_first(a, b):
	return -b/a

print("Program solve first oder equation\n")

a = int(input("a = "))
while a == 0:
	print("a can't equal 0 ! Enter again...")
	a = int(input("a = "))
b = int(input("b = "))
print("x = "+ str(equation_first(a, b)))

