def printA():
    result = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
                result += "*"
            else:
                result += " "
        result += "\n"
    return result

print(printA())