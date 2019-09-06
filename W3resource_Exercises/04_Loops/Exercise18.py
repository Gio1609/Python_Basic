def printD():
    result = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (column == 1) or (column == 5 and row != 0 and row != 6) or ((row == 0 or row == 6)and column in range(1, 5)):
                result += "*"
            else:
                result += " "
        result += "\n"
    return result


print(printD())