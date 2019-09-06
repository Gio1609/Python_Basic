def Multiply(list):
    Mul = 0
    for n in list:
        Mul *= n
    return Mul

list = [8, 2, 3, -1, 7]
print(Multiply(list))