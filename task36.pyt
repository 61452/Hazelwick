import random

number = random.randint(1,100)
guess=int(input("guess a number between 1 and 100:"))
count = 0
while guess != number and count < 10:
    if guess < number:
        print("too low")
    else:
        print("too high")
    guess=int(input("guess a number between 1 and 100: "))
    count += 1
if guess == number:
    print("you guessed it!")
else:
    print("you ran out of guesses! the number was", number)