import random

choice = ['r','p','s']

user_choice = input('Rock,paper,scissors? (r/p/s):').lower()
if user_choice not in choice:
    print('Invalid Choice! ')
random.choice = random.choice(choice)