from random import randint
import sys

name = input("What's your name? ")
print("Nice to meet you " + str(name) + "! It'll be $5 per game.")

play = "yes"
pot = 5
i=1
bank = 50

while play == "yes":
    p1=randint(1,6)
    p2=randint(1,6)
    print("Round " + str(i))
    print("Amount in Bank: $" + str(bank) + ".00")
    print("Amount in Pot: $" + str(pot) + ".00")
    print("The house rolls: " + str(p2))
    print("You roll: " + str(p1))
    if (p1 > p2):
        print("You win!")
        bank = ((bank - 5) + pot)
        print("New Bank Amount: $" + str(bank) + ".00")
        play = input("Continue? ")
        if (play == "yes"):
            pot = (pot * 2)
            i+=1
            print("The pot is doubled: $" + str(pot) + ".00")
        elif (play == "no"):
            print("Your total winnings: $" + str(pot) + ".00")
        else:
            while play not in ["yes","no"]:
                play = input("I'm sorry, I don't understand. Please respond with yes or no: ")
    else:
        print("You lose...")
        bank = (bank - 5)
        print("New Bank Amount: $" + str(bank) + ".00")
        play = input("Play a new round? ")
        if (play == "yes"):
            i=1
            pot=5
        elif (play == "no"):
            break
        else:
            while play not in ["yes","no"]:
                play = input("I'm sorry, I don't understand. Please respond with \"yes\" or \"no\": ")
