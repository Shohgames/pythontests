#__init__ is a initializer, self is the  

class Rectangle:
    def __init__(self, x, y):
        self.test = x
        self.y = y

rect1 = Rectangle(2, 3)
rect2 = Rectangle(10, 20)

print("rect1.test =", rect1.test)  # 2
print("rect1.y =", rect1.y)        # 3
print("rect2.test =", rect2.test)  # 10  
print("rect2.y =", rect2.y)        # 20

rect1.test = 999
print("After changing rect1.test:")
print("rect1.test =", rect1.test)  # 999
print("rect2.test =", rect2.test)  # still 10!