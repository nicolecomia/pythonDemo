# Demo of basic input in python
name = input("Enter your name: ")
print("Hello " + name)

# Demo of a program that computes for an area of a circle
radius = float(input("Enter the radius: "))
area = 3.14 * (radius**2)
print("The area of the Circle is: " + str(area))

# Demo of a program that computes for a volume of a cylinder
radius = float(input("Enter the Radius: "))
height = float(input("Enter the Height: "))
volume = 3.14 *(radius**2 * height)
print("The Volume of the Cylinder: " + str(volume))



#sample text-based game with simple conditional statement
character_health = 100

name = input("Enter your name: ")
print("Hello " + name)

v = int(input("Choose 1 if you want to cross the river\nChoose 2 if you want to jump on the ravine\nInput: "))
if v == 1:
    print("You have crossed the river")
elif v == 2:
    print("You have jumped into the ravine")
    print("Your character has taken 10pt of damage")
    character_health = character_health - 10
else:
    print("Invalid input")

print("Your character's Health: " + str(character_health))







