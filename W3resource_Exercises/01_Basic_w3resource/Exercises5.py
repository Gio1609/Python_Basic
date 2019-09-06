import calendar
from datetime import date

y = int(input("Enter into year = "))
m = int(input("Enter into month = "))
print(calendar.month(y, m))
print("\nSelect any tow dates")
f_d = int(input("\tEnter date firt: "))
s_d = int(input("\tEnter date second: "))

date1 = date(y, m, f_d)
date2 = date(y, m, s_d)
delta = date2 - date1
print("\nBetween of tow dates is : ", delta.days)

