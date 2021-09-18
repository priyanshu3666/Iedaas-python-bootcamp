def gen_fibbo(num):
    a=0
    b=1
    for i in range(num):
        yield a
        a,b = b,a+b

for x in gen_fibbo(8):
    print(x)

    
