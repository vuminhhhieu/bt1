import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def area(self):
        return math.pi * self.radius ** 2


    shape = input("Enter the shape (rectangle or circle): ")
    
    if shape == "rectangle":
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        
        rect = Rectangle(width, height)
        print(f"Perimeter of the rectangle: {rect.perimeter()}")
        print(f"Area of the rectangle: {rect.area()}")
    
    elif shape == "circle":
        radius = float(input("Enter the radius of the circle: "))
        
        circ = Circle(radius)
        print(f"Perimeter of the circle: {circ.perimeter()}")
        print(f"Area of the circle: {circ.area()}")
    
    else:
        print("Invalid shape entered. Please enter 'rectangle' or 'circle'.")


