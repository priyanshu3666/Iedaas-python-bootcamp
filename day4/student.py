class Student():
  def __init__(self,name,roll):
    self.name = name
    self.roll= roll
  def display(self):
    print(self.name)
    print(self.roll)
  def setAge(self,age):
    self.age=age
  def setMarks(self,marks):
    self.marks = marks

stuu =Student("priyanshu",50)
stuu.display()