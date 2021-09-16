class Times():

  def __init__(self, hours, mins):
    self.hours = hours
    self.mins = mins

  def addTime(t1, t2):
    t3 = Times(0,0)
    if t1.mins+t2.mins > 60:
      t3.hours = (t1.mins+t2.mins)/60
    t3.hours = t3.hours+t1.hours+t2.hours
    t3.mins = (t1.mins+t2.mins)-(((t1.mins+t2.mins)/60)*60)
    return t3

  def displayTime(self):
    print ("Time is",self.hours,"hours and",self.mins,"minutes.")

  def displayMinute(self):
    return self.hours*60+self.mins

a = Times(4,20)

a.displayTime()
a.displayMinute()