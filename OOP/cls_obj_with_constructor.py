# just using constructor
class Book1:
    def __init__(self, color):   # constructor
        self.color = color
 
OOP = Book1("red")  #obj1
print(OOP.color)   #red
# print(Book("sky color").color)  #sky color


# multi args without using __repr__()/__str__()
class Book1:
    def __init__(self, color, price):   # constructor
        self.color = color
        self.price = price
 
OOP = Book1("red", 500)  #obj1
print(OOP.color)   #red
print(OOP.price)   #500
# print(OOP.color, OOP.price)  # red 500

# if we use __repr__()/__str__(),we can directly get 
# red
# 500
# by using only   ----> print(algo) 


