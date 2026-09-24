N1=int(input("enter a number of minutes"))
N2= N1//60
N3= N1%60
print("The time is", N2, "hours and", N3, "minutes")
if N1<120:
    print("The time is", N2, "hour and", N3, "minutes")