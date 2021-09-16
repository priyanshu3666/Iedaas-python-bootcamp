from collections import defaultdict

mydict = defaultdict(lambda : "this key does not exist")
mydict['name'] = "priyanshu"
mydict['rollno'] = 50
mydict['age'] =22

print(mydict['name'])
print(mydict['class'])