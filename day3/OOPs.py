class Dog():
    species  = 'mammal'
    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots
    def bark(self):
        print("woof! My name is {}".format(self.name))

my_dog = Dog('Lab','nikhil','No Spots')
print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)
my_dog.bark()




class Circle():
    pi =  3.14
    def  __init__(self,radius):
        self.radius = radius
        self.area =radius*radius*Circle.pi
        
    def circumference(self):
        return Circle.pi *self.radius * 2

circle_obj = Circle(5)
print(circle_obj.circumference())
        




#special magic / Dendor methods

class Book():
    def __init__(self,title,author,pages):
        self.title =title
        self.author = author
        self.pages =pages
    
    def __str__(self):
        return f"{self.title} by  {self.author}"
    
    def __len__(self):
        return self.pages

book_obj =  Book('python', 'Priyanshu',200)

print(book_obj)
str(book_obj)
print(len(book_obj))




# Problem 1
# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

class Line(object):
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)


cordinate1 = (3,2)
cordinate2 = (8,10)
line = Line(cordinate1,cordinate2)
print(line.distance())
print(line.slope())


 # problem 2 
class Cylinder():
    pi = 3.14
    def __init__(self,height,radius):
        self.height = height
        self.radius = radius
    
    def volume(self):
        return self.height*Cylinder.pi*self.radius**2

    def surface_area(self):
        return 2*Cylinder.pi*self.radius*(self.height + self.radius)

cylinder = Cylinder(2,3)
print(cylinder.volume())
print(cylinder.surface_area())



# For this challenge, create a bank account class that has two attributes:

# owner
# balance
# and two methods:

# deposit
# withdraw
# As an added requirement, withdrawals may not exceed the available balance.

# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

print()
print()
print()
print()
print()

class Bank():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
            self.balance +=amount
            print("congratulation you have deposit Rs. {}".format(amount))
        
    
    def withdrawl(self,amount):
        if amount < self.balance:
            self.balance -=amount
            print("congratulation you have withdrawl  Rs. {}".format(amount))
        else:
            print("the amount is excess than balance ")
        

    
operation = Bank('Priyanshu',1000)
print(operation.balance)
operation.withdrawl(5000)
print(operation.balance)
operation.deposit(5000)
print(operation.balance)

def oop():
    print("i am inside  oops")