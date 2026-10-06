a = float(input("Enter the first side length: "))
b = float(input("Enter the second side length: "))
c = float(input("Enter the third side length: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid triangle: side lengths must be positive.")
elif a + b <= c or a + c <= b or b + c <= a:
    print("These lengths do not form a triangle.")
elif a == b == c:
    print("This triangle is equilateral.")
elif a == b or b == c or a == c:
    print("This triangle is isosceles.")
else:
    print("This triangle is scalene.")
