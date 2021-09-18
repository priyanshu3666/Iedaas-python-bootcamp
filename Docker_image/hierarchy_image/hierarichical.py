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
