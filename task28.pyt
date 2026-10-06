temp=int(input("Enter a temperature value: "))
if temp < 0:
    print("The temperature is below freezing.")
elif temp >= 0 and temp < 100:
    print("The temperature is cold.")
elif temp >= 21 and temp < 100:
    print("The temperature is warm.")
elif temp >= 30 and temp < 100:
    print("The temperature is hot.")
else:
    print("enter a valid temperature value.")