Hours = -1
total = 0
while Hours < 0:
    Hours= int(input("Enter the number hours parked: "))
    choice=input ("Enter the type of vehicle (Electric/Gasoline): ")
if choice.lower() == "electric":
    cost = Hours * 2
elif choice.lower() == "gasoline":
    cost = Hours * 4
print("The total cost for parking is: £" + str(cost))

