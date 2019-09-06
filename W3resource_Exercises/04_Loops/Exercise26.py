def printS_01():
    result = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (row == 0 and (column > 0 and column < 5)) or (row == 3 and (column > 0 and column < 4)) or (row == 6 and column < 4) or (column == 0 and (row == 1 or row == 2)) or (column == 4 and (row == 4 or row == 5)):
                result += "*"
            else:
                result += " "
        result += "\n"
    return result

print(printS_01())