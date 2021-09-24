import random
# Demo of basic input in python
# name = input("Enter your name: ")
# print("Hello " + name)

# Demo of a program that computes for an area of a circle
# radius = float(input("Enter the radius: "))
# area = 3.14 * (radius**2)
# print("The area of the Circle is: " + str(area))

# Demo of a program that computes for a volume of a cylinder
# radius = float(input("Enter the Radius: "))
# height = float(input("Enter the Height: "))
# volume = 3.14 *(radius**2 * height)
# print("The Volume of the Cylinder: " + str(volume))

#Demo for array 
# fruits = ["apple", "banana", "cherry", "strawberry", "melon", "watermelon"]
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])

#Demo for for Loop
# for x in fruits:
#     print(x)

# i = 0
# while i < 10:
#     print("Hello World")
#     print(i)
#     i = i + 1



#sample text-based game with simple conditional statement
character_health = 100
item = ""

name = input("Enter your name: ")
print("Hello " + name)

while character_health > 0:
    if character_health != 100 and item == "Fish":
        n = input("You have taken some damage to heal select [1 to heal/ 0 to ignore]")
        if n == "1":
            character_health += 10
            print("Your character's health is back to " + str(character_health))
        else :
             print("Your character's health is back to " + str(character_health))


    v = int(input("Choose 1 if you want to cross the river\nChoose 2 if you want to jump on the ravine\nChoose 3 if you want to fight monster in the dungeon \nInput: "))
   
    #Start of Journey
    if v == 1: 
        choice = input("If you want to go fishing select [1 for yes/ 0 for no]")
        if choice == "1":
            #Fishing minigame
            print("You have chosen Fishing! ")
            chance = random.randint(0,9)
            if chance > 6:
                item = "Fish"
                print("You have catch a Fish!")
            else:
                print("There is no fish to catch")

        elif choice == "0":
            print("You have crossed the river")


    elif v == 2:
        #damages the player
        print("You have jumped into the ravine")
        print("Your character has taken 10pt of damage")
        character_health = character_health - 10
    elif v == 3:
        #damages the player
        print("You have enter the dungeon")

    else:
        print("Invalid input")

    print("Your character's Health: " + str(character_health))

print("Your Character is dead!")







