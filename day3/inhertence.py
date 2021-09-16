'''
THis code is written by Priyanshu Shukla for the implementation of inheritence
'''

# this is multilevel inheritence

class Class1():
    def __init__(self):
        self.classname = 'Class1'
    def method(self):
        print(" this method is of class 1")
    def class1(self):
        print("ths is class 1 ")

    
class Class2(Class1):
    def __init__(self):
        self.classname = 'class2'
    def method(self):
        super().method()
        print("this method is of class 2")
    
class Class3(Class2):
    def __init__(self):
        self.classname = 'class3'
    def method(self):
        super().method()
        print("this method is of class 3")


class1 = Class1()
class2 = Class2()
class3 = Class3()
class2.method()
class3.class1()  


# this is multiple inheritence
class Summation():
    def __init__(self):
        print("summation class initialized")  
    def Summation(self,a,b):  
        return a+b;  
    def m1(self):
        print("this method is of summation class")

class Mulultiplication():  
    def __init__(self):
        print("multiplication class initialized")  
    def Multiplication(self,a,b):  
        return a*b
    def m1(self):
        print("this method is of multipication  class")
      
class Divide(Summation,Mulultiplication):
    def __init__(self):
        print("divide class initialized")  
    def Divide(self,a,b):  
        return a/b;  
class Modulus(Mulultiplication,Summation):
    def __init__(self):
        print("modulus class initialized")

modulus_ = Modulus()
divide_ = Divide()  
print(divide_.Summation(10,20))  
print(divide_.Multiplication(10,20))  
print(divide_.Divide(10,20))  
divide_.m1()
modulus_.m1()




#hierarchical inheritence

class Parent:
	def func1(self):
		print("This function is inside parent class.")


class Child1(Parent):
	def func2(self):
		print("This function is inside ichild 1.")


class Child2(Parent):
	def func3(self):
		print("This function is inside  child 2.")


object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()
