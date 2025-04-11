"""
__init__  --> __init__ sets the values when object is created.
             obj = Class()
             auto-called when object is created.

__str__  --> print(obj)
             when you print the object,
             What to show on the screen
             Inspect/debug/show obj	Developer-friendly / unambiguous

__repr__  --> print(obj)	Human-friendly
             No extra parameters are passed to __repr__()
             — it just uses self.
__len__  --> len(obj)

__add__  -->  Add two objects	
              obj1 + obj2

__eq__  --> Compare objects with ==
            obj1 == obj2


"""
# ---------> just using constructor <-------------
class Book1:
    def __init__(self, color):   # constructor
        self.color = color
 
OOP = Book1("red")  #obj1
print(OOP.color)   #red
# print(Book("sky color").color)  #sky color


# ---------> using __repr__  <-------------
class Book2:
    def __init__(self, color,price):   # constructor
        self.color = color
        self.price = price

    def __repr__(self):   # only self needed here
         return f'{self.color} and {self.price}'

algo = Book2("blue", 500)  # creating object
print(algo)  # Output: blue and 500
# Python will automatically call:Book.__repr__() 



# --------->   __str__   <-------------
class Book3:
    def __init__(self, color,price):   
        self.color = color
        self.price = price

    def __str__(self):   # only self needed here
         return f'{self.color} and {self.price}'

algo = Book3("blue", 500)  # creating object
print(algo)  # Output: blue and 500
# Python will automatically call:Book.__str__() 



# ---------> using __repr__   <-------------
class Book2:
    def __init__(self, color,price):   # constructor
        self.color = color
        self.price = price 

    def __repr__(self):   # only self needed here
         return f'{self.color} and {self.price}'
    
    def __str__(self):   # only self needed here
         return f'{self.color} & {self.price}'     

algo = Book2("blue", 500)  # creating object
print(algo)  # Output: blue & 500
# Python will automatically call:Book.__repr__() 



# ---------> using both __str__() and __repr__() at the same time  <-------------
# __str__() will be called first.
# print(algo) will call __str__()
#  (because print() looks for a user-friendly output first).
class Book4:
    def __init__(self, color,price):   # constructor
        self.color = color
        self.price = price 

    def __repr__(self):   # only self needed here
         return f'this is repr dunder method, {self.color} & {self.price}'
    
    def __str__(self):   # only self needed here
         return f'this is str dunder method, {self.color} & {self.price}'    

algo = Book4("blue", 500)  # creating object
print(algo)  
# Output : ???  
# this is str dunder method, blue & 500
 

