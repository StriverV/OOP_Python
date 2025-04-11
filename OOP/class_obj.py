class Book:

    color = "red"
    price = 500
       
print(Book.color)  # red

p = Book.price 
print(Book.price)  # 500


algo = Book()  #obj1
c = algo.color = "blue"
print(c)   #blue


OOP = Book()  #obj1
c2 = OOP.color = "sky color"
print(c2)   #blue