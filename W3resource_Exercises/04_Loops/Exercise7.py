def Solution(datalist):
    for item in datalist:
        print ("Type of ",item, " is ", type(item))


datalist =  [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
Solution(datalist)