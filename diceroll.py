from random import randint

i=1
r=randint(1,6)

while r != 1:
    r=randint(1,6)
    print("Roll " + str(i) + ": " + str(r))
    i += 1
