score=0

import random

number1 = random.randint (0,100)

number2 = random.randint (0,100)

number3 = random.randint (0,100)

number4 = random.randint (0,100)

number5 = random.randint (0,100)

guess1=int(input("guess the first randomly generated number 1-100: "))

guess2=int(input("guess the second randomly generated number 1-100: "))

guess3=int(input("guess the third randomly generated number 1-100: "))

guess4=int(input("guess the fourth randomly generated number 1-100: "))

guess5=int(input("guess the fifth randomly generated number 1-100: "))

difference1=abs(number1-guess1)
difference2=abs(number2-guess2)
difference3=abs(number3-guess3)
difference4=abs(number4-guess4)
difference5=abs(number5-guess5)

if guess1 == number1:
    print("Bang on!")
    score += 10

elif difference1 <= 5:
    print("Close!")
    score += 5

elif difference1 <= 10:
    print("okay")
    score += 2

elif difference1 <= 11:
    print("way off!")
    score += 1

if guess2 == number2:
    print("Bang on!")
    score += 10

elif difference2 <= 5:
    print("not too far off!")
    score += 5

elif difference2 <= 10:
    print("Not too far off!")
    score += 2

elif difference2 <= 11:
    print("way off!")
    score += 1

elif difference2 <= 5:
    print("Close!")
    score += 5

elif difference2 <= 10:
    print("Not too far off!")
    score += 2

elif difference2 <= 11:
    print("way off!")
    score += 1

if guess3 == number3:
    print("Bang on!")
    score += 10

elif difference3 <= 5:
    print("Close!")
    score += 5
elif difference3 <= 10:
    print("Not too far off!")
    score += 2
elif difference3 <= 11:
    print("way off!")
    score += 1

if guess4 == number4:
    print("Bang on!")
    score += 10
elif difference4 <= 5:
    print("Close!")
    score += 5
elif difference4 <= 10:
    print("Not too far off!")
    score += 2
elif difference4 <= 11:
    print("way off!")
    score += 1


elif difference4 <= 10:
    print("Not too far off!")
    score += 2

elif difference4 <= 11:
    print("way off!")
    score += 1


if guess5 == number5:
    print("Bang on!")
    score += 10

elif difference5 <= 5:
    print("Close!")
    score += 5

elif difference5 <= 10:
    print("Not too far off!")
    score += 2

elif difference5 <= 11:
    print("way off!")
    score += 1

print(f"the first number was {number1}")

print(f"the second number was {number2}")

print(f"the third number was {number3}")

print(f"the fourth number was {number4}")

print(f"the fifth number was {number5}")

print(f"your guesses were {guess1}, {guess2}, {guess3}, {guess4}, {guess5}")

print(f"your score is {score} out of 50")

