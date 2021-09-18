import random

def random_generator(low,high,num):
    for i in range(num):
        yield random.randint(low,high)

for x in random_generator(1,12,5):
    print(x)