def hcf(a, b):
    if(b == 0):
        return a
    else:
        return hcf(b, a % b)
  
a = 5
b= 20

print(f"The gcd of {a} and {b} is : ", end="")
print(hcf(a,b))

