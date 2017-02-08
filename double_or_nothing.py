from random import randint
import sys

name = input("What's your name? ")
print("Nice to meet you " + name + "!")

play = "yes"
wager = input("Enter your initial wager: ")

while play == "yes":
    i=1
    p2=randint(1,6)
    print("Round " + str(i)
    print("Player 2 rolls: " + str(p2))
