from math import radians
import random

print(random.randint(1,20))

# print(random.seed(101))
print(random.randint(1,20))
print(random.randint(1,20))
print(random.randint(1,20))
print(random.randint(1,20))
#random.seed(20)
print(random.randint(1,20))
mylist  = [x for x in range(21)]
print(mylist)
print(random.choices(population =mylist,k=12))
print(random.sample(mylist,k=8))
random.shuffle(mylist)
print(mylist)

print(random.uniform(a=10,b=20))

print(random.gauss(mu = 0,sigma=1))