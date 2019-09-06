def ReverseString(str):
    result = ""
    for c in range(len(str)-1, -1, -1):
        result += str[c]
    return result

str = input("Enter a string : ")
print(ReverseString(str))
