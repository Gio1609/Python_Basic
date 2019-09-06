def CountNumber(arr):
    even, odd = 0, 0
    for n in arr:
        if n % 2 == 0:
            odd += 1
        else:
            even += 1
    print("Number of odd numbers :",odd)
    print("Number of even numbers :",even)

arr = (1, 2, 3, 4, 5, 6, 7, 8, 9)
CountNumber(arr)
