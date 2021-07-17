# Author : Anil Shrestha
# its only for educational purpose
# its a snake water gun game coded in python
# any inerested begineer programmer are allowed  modify the codes
import random
# ramdom helps to pick random selection


def game(com, you):
    if com == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif com == "w":
        if you == "s":
            return True
        elif you == "g":
            return False
    elif com == "g":
        if you == "w":
            return True
        elif you == "s":
            return False
    elif com == you:
        return None


# Two players a(computer) and b
print("Snake Water or Gun game: ")
print("Computer's Turn: Snake(1) Water(2) or Gun(3) ?")
# computer selection
a = random.randrange(1, 4)
if a == 1:
    a = "s"
elif a == 2:
    a = "w"
elif a == 3:
    a = "g"
# user input(selection)
b = input(" Your Turn: Snake(s) Water(w) or Gun(g) ? \n")

stat = game(a, b)
# analysing status A/C to value received from game function
if stat == None:
    print("Tie!")
elif stat == True:
    print("you win!")
else:
    print("you lost!")

# printing selections
print(f"Computer choose = {a}")
print(f"You Choose = {b}")
