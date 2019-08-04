"""
Assumption :
1/01/0001 was Monday
Every month has 31 days
Every year has 365 days

"""


x = int(input("Enter day"))
y = int(input("Enter month"))
z = int(input("Enter year"))
r1 = x + (31 * (y-1))
r2 = (365 * (z-1)) - 1
result = (r1 + r2)%7
if result == 0:
    print("Monday")
if result == 1:
    print("Tuesday")
if result == 2:
    print("Wednesday")
if result == 3:
    print("Thurday")
if result == 4:
    print("Friday")
if result == 5:
    print("Saturday")
if result == 6:
    print("Sunday")
print(result)
