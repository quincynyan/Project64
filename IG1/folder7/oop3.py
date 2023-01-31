class Rectangle:
    length = 0
    width = 0
    area = 0
     
 
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color
     
    def display(self):
        print("Length is : " + str(self.length))
        print("Width is : " + str(self.width))
        print("Color is : " + self.color)
        print("Area is : " + str(self.area))
 
    def calculatearea(self):
        self.area = self.length * self.width
 
# creating object of the class
# this will invoke parameterized constructor
rectangleLength = int(input("Enter Length : "))
rectangWidth = int(input("Enter Width : "))
rectangColor = input("Enter Color : ")
print("------------Answer----------")
obj = Rectangle(rectangleLength, rectangWidth, rectangColor)
 
# perform calculate
obj.calculatearea()
 
# display result
obj.display()
