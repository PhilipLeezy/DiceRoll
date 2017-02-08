from random import randint
import sys

name = input("What's your name? ")
print("Nice to meet you " + name + "!")

play = "yes"
pot = 5

while play == "yes":
    i=1
    p1=randint(1,6)
    p2=randint(1,6)
    print("Round " + str(i))
    print("Amount in Pot: $" + str(pot) + ".00")
    print("The house rolls: " + str(p2))
    print("You roll: " + str(p1))
    if (p1 > p2):
        print("You win!")
        play = input("Continue? ")
        if (play == "yes"):
            pot = (pot * 2)
            print("The pot is doubled: $" + str(pot) + ".00")
        else:
            print("Your winnings: $" + str(pot) + ".00")
    else:
        print("You lose...")
