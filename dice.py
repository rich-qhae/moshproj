import random

while True:
#ask user for input
  choice= input("Roll the dice (y/n): ").lower()
#Using conditionals to determine random dice numbers
  if choice == "y":
    dice1 =random.randint(1,6)
    dice2 = random.randint(1,6)
    print (f'({dice1}, {dice2})')
  elif choice == "n":
    print("Thank you for playing the game!")
    break
  else:
    print("invalid Choice")

