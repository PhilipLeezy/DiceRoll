from random import randint

i = 1
r = None

while r != 1:
    i += 1
    r = randint(1,6)
    print("Roll " + str(i) + ": " + str(r))
