class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
            return self.length*self.breadth
    def perimeter(self):
            return 2*(self.length+self.breadth)
l=float(input("enter length of rectangle:")) 
b=float(input("enter breadth of rectangle:"))
rect=Rectangle(l,b)
print("Area of rectangle:",rect.area())
print("Perimeter of rectangle:",rect.perimeter())
    
    

