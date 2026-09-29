Score=0
Addition = int(input("What is 64 add 36: "))
Subtraction = int(input("What is 34 subtract 20?:"))
Division = int(input("What is 48 divided by 2?: "))
Multiplication = int(input("What is 4 multiplied by 10?: "))

if Addition == 100:
    print("correct!")
    Score += 1
else:
    print("incorrect")

if Subtraction == 14:
    print("correct!")
    Score += 1
else:
    print("incorrect")

if Multiplication == 40:
    print("correct!")
    Score += 1
else:
    print("incorrect")

if Division == 24:
    print("correct!")
    Score += 1
else:
    print("incorrect")

print(f"Your Score is {Score}")