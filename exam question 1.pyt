riderlimit = 0

while riderlimit < 8:
    height = int(input("Enter your height in cm: "))

    if height > 140:
        print("You can ride!")
        riderlimit += 1
    elif 120 <= height <= 140:
        answer = input("Do you have an adult with you? (yes/no): ").strip().lower()
        if answer == "yes":
            adult=int(input("how many adults are with you? "))
            print("You can ride!")
            riderlimit += adult
        else:
            print("You cannot ride without an adult. Try again.")
    else:
        print("You are too short to ride. Try again.")