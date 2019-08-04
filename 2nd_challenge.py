"""
Assumption :
1/01/0001 was Monday
Every month has 31 days
Every year has 365 days

"""


x = int(input("Enter day"))
y = int(input("Enter month"))
z = int(input("Enter year"))
r1 = x

if y == 1 :
    r1 = x % 7
    if r1 == 1:
        print("Its monday-0")
    elif r1 == 2:
        print("Its tuesday-1")
    elif r1 == 3:
        print("Its wednesday-2")
    elif r1 == 4:
        print("Its thursday-3")
    elif r1 == 5:
        print("Its Friday-4")
    elif r1 == 6:
        print("Its Saturday-5")
    elif r1 == 0:
        print("Its Sunday-6")
elif y == 2:
    r1 = (r1+3)%7
    if r1 == 1:
        print("Its monday-0")
    elif r1 == 2:
        print("Its tuesday-1")
    elif r1 == 3:
        print("Its wednesday-2")
    elif r1 == 4:
        print("Its thursday-3")
    elif r1 == 5:
        print("Its Friday-4")
    elif r1 == 6:
        print("Its Saturday-5")
    elif r1 == 0:
        print("Its Sunday-6")

elif y == 3:
    r1 = (r1+6)%7
    if r1 == 1:
        print("Its monday-0")
    elif r1 == 2:
        print("Its tuesday-1")
    elif r1 == 3:
        print("Its wednesday-2")
    elif r1 == 4:
        print("Its thursday-3")
    elif r1 == 5:
        print("Its Friday-4")
    elif r1 == 6:
        print("Its Saturday-5")
    elif r1 == 0:
        print("Its Sunday-6")

elif y == 4:
    r1 = (x+2) % 7
    if r1 == 1:
        print("Its monday-0")
    elif r1 == 2:
        print("Its tuesday-1")
    elif r1 == 3:
        print("Its wednesday-2")
    elif r1 == 4:
        print("Its thursday-3")
    elif r1 == 5:
        print("Its Friday-4")
    elif r1 == 6:
        print("Its Saturday-5")
    elif r1 == 0:
        print("Its Sunday-6")
elif y == 5:
    r1 = (x + 5) % 7
    if r1 == 1:
        print("Its monday-0")
    elif r1 == 2:
        print("Its tuesday-1")
    elif r1 == 3:
        print("Its wednesday-2")
    elif r1 == 4:
        print("Its thursday-3")
    elif r1 == 5:
        print("Its Friday-4")
    elif r1 == 6:
        print("Its Saturday-5")
    elif r1 == 0:
        print("Its Sunday-6")
elif y == 6:
    r1 = (r1 + 6)%7
    if r1 == 1:
        print("Its monday-0")
    elif r1 == 2:
        print("Its tuesday-1")
    elif r1 == 3:
        print("Its wednesday-2")
    elif r1 == 4:
        print("Its thursday-3")
    elif r1 == 5:
        print("Its Friday-4")
    elif r1 == 6:
        print("Its Saturday-5")
    elif r1 == 0:
        print("Its Sunday-6")
elif y == 7:
    r1 = (x + 2) % 7
    if r1 == 1:
        print("Its monday-0")
    elif r1 == 2:
        print("Its tuesday-1")
    elif r1 == 3:
        print("Its wednesday-2")
    elif r1 == 4:
        print("Its thursday-3")
    elif r1 == 5:
        print("Its Friday-4")
    elif r1 == 6:
        print("Its Saturday-5")
    elif r1 == 0:
        print("Its Sunday-6")
elif y == 8:
    r1 = (x + 5) % 7
    if r1 == 1:
        print("Its monday-0")
    elif r1 == 2:
        print("Its tuesday-1")
    elif r1 == 3:
        print("Its wednesday-2")
    elif r1 == 4:
        print("Its thursday-3")
    elif r1 == 5:
        print("Its Friday-4")
    elif r1 == 6:
        print("Its Saturday-5")
    elif r1 == 0:
        print("Its Sunday-6")
elif y == 9:
    r1 = (r1 + 6) % 7
    if r1 == 1:
        print("Its monday-0")
    elif r1 == 2:
        print("Its tuesday-1")
    elif r1 == 3:
        print("Its wednesday-2")
    elif r1 == 4:
        print("Its thursday-3")
    elif r1 == 5:
        print("Its Friday-4")
    elif r1 == 6:
        print("Its Saturday-5")
    elif r1 == 0:
        print("Its Sunday-6")

elif y == 10:

    r1 = (x + 2) % 7
    if r1 == 1:
        print("Its monday-0")
    elif r1 == 2:
        print("Its tuesday-1")
    elif r1 == 3:
        print("Its wednesday-2")
    elif r1 == 4:
        print("Its thursday-3")
    elif r1 == 5:
        print("Its Friday-4")
    elif r1 == 6:
        print("Its Saturday-5")
    elif r1 == 0:
        print("Its Sunday-6")
elif y == 11:
    r1 = (x + 5) % 7
    if r1 == 1:
        print("Its monday-0")
    elif r1 == 2:
        print("Its tuesday-1")
    elif r1 == 3:
        print("Its wednesday-2")
    elif r1 == 4:
        print("Its thursday-3")
    elif r1 == 5:
        print("Its Friday-4")
    elif r1 == 6:
        print("Its Saturday-5")
    elif r1 == 0:
        print("Its Sunday-6")
elif y == 12:
    r1 = (r1 + 6) % 7
    if r1 == 1:
        print("Its monday-0")
    elif r1 == 2:
        print("Its tuesday-1")
    elif r1 == 3:
        print("Its wednesday-2")
    elif r1 == 4:
        print("Its thursday-3")
    elif r1 == 5:
        print("Its Friday-4")
    elif r1 == 6:
        print("Its Saturday-5")
    elif r1 == 0:
        print("Its Sunday-6")
