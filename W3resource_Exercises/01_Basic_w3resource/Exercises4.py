name = str(input("Enter to fill name : "))
arr = name.split(" ")
print("Array entered :")
print(arr)
arr2 = []
i = len(arr)
while (i > 0):
	i = i-1
	arr2.append(arr[i])
print("Array reversed :")
print(arr2)