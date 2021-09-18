def create_cube(last_num):
    for x in range(last_num):
        yield x**3

for i in create_cube(5):
    print(i)