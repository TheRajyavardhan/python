class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Name: ",self.name)
        print("Marks: ", self.marks)

s1 = Student("Mohit",92)
s2 = Student("Dev",85)

s1.display()
s2.display()

class Rectangle:
    shape = "Rectangle"

    def __init__(self,rec_len,rec_width):
        self.length = rec_len
        self.breadth = rec_width
    def area(self):
        return self.length*self.breadth
    def parameter(self):
        return 2*(self.length+self.breadth)

rec_one = Rectangle(30,20)    
rec_two = Rectangle(40,20)

print("Area: ",rec_one.area())
print("Parameter: ",rec_one.parameter())

print("Area: ",rec_two.area())
print("Parameter: ",rec_two.parameter())

print("shape of figure: ",rec_one.shape)