
PI = 3.14
r = float(input("Enter the radius of a circle:"))
area = PI * r * r
print("Area of a circle = %.2f" %area)


def circleArea(r):
    PI = 3.14
    return PI * (r * r)

radius = 5  # Replace with your desired radius
area = circleArea(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}")
#
