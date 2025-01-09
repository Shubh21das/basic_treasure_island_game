# This is a Treausre finding game where the user has to make choices to find the treasure.

print("Welcome to the treaure island !\nYou are on the mission to find the treaure\nMake choices and it will lead to your destiny either treaure or death")
c1 = input("you are the road and you see two paths, which you want to take ! Left or right: ").lower()
if c1 == "left":
    c2 = input("You have reached the lake, do you want to swim or wait for the boat ? Swim or wait: ").lower()
    if c2 == "wait":
        c3 = input("You have reached the island and you see three doors, which one you want to open ? Red, Blue or Yellow: ").lower()
        if c3 == "yellow":
            print("Congratulations, you have found the treasure !")
        elif c3 == "red":
            print("You are burned by fire, Game Over !")
        elif c3 == "blue":
            print("You are eaten by beasts, Game Over !")
        else:
            print("You have chosen the wrong door, Game Over !")
    else:
        print("You are attacked by the crocodile, Game Over !")
else:
    print("You are fall into the pit, Game Over !")

print("Thank you for playing the game !")  