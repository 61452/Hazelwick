total=0
attempts=0

import random
number=random.randint(1,100)

for i in range(10):
    guess=int(input("enter a guess: "))
    attempts = 1

    if number <1 or guess > 100 and attempts < 10:
        print("your guess was too high")
        attempts += 1
    elif number > guess and attempts < 10:
        print("your guess was too low")
        attempts += 1
    elif number == guess:
        print("you guessed the number")
        break



