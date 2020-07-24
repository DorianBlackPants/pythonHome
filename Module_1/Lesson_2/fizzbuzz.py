fizz = int(input("Type the first number here: "))
buzz = int(input("Type the second number here: "))
n = int(input("Type the third number here: "))
list_1 = []

for i in range (1,n+1):
    if not i%fizz and not i%buzz:
        list_1.append("FB")
    elif not i%buzz:
        list_1.append("B")
    elif not i%fizz:
        list_1.append("F")
    else:
        list_1.append(i)

print(" ".join(str(x) for x in list_1))


