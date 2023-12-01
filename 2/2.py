a = int(input())
b = int(input())

# Завдання 1
c1 = (a + b) * (a * b)
if c1 > 100:
    print ("yes")
else:
    print ("no")

# Завдання 2
c2 = (a + b) * (a - b)
if c2 > 100:
    print (c2)
else:
    print (c2 * 2)

# Завдання 3 
c3 = (a + b) * (a * b)
if c3 != 100:
    if c3 < 5:
        print (c3)
    else:
        print(c3 * 2)

# Завдання 4
c4 = (a + b) / (a * b)
if c4 != 45:
    if c4 < 100:
        print (c4)
    else:
        print (c4 * 2)

# Завдання 5
c5 = (a + b ) / a
if c5 > 100:
    print ("yes")
elif c5 != 10:
    print ("no")