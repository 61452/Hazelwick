total=0
attempts=0
import random
number=random.randint(1,100)
while True:
    guess=int(input("enter a guess"))
    count=1
    if number > guess:
        print("your guess was too high")