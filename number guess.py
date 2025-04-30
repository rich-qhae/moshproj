import random 

numberGuess = random.randint (1,200)

while True:
    try:
        guess = int(input("Guess a number between 1 and 200? "))
        if guess > numberGuess :
            print('Too high!')
        elif guess < numberGuess:
            print ('Too low')
            break
        else:
            print('Try again')
    except ValueError:
        print("Please enter a valid number")
  

