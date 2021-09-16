#write a function called myfunc that prints the string  'Hello World'

def myfunc():
    print('Hello World')

myfunc()

# wite a function that takes a name as input and print as 'hello name'
def myfunc(name):
    print('Hello {}'.format(name))

# return according to bool value , bool_value == True > "Hello" else "Goodbye"
def myfunc(Bool_value):
    if Bool_value == True:
        return "Hello"
    elif Bool_value == False:
        return "Goodbye"

# takes three argumeent and check z if true return z else y
def myfunc(x,y,z):
    if z == True :
        return x
    else:
        return y
#return sum f given argument
def myfunc(num1,num2):
    return num1+num2

#check given argument is even or not
def is_even(n):
    if n%2==0:
        return True
    else:
        return False


#check greater and return false if firstt argument is not greater than second one 
def is_greater(x, y):
    return x>y

#*args given and return sum of *args
def myfunc(*args):
    return sum(args)


#takes multiple arguments  and return even output 
output = []
def myfunc(*args):
    for a in args:
        if a%2 == 0:
            output.append(a)
    return output
    




# Functions #10: skyline
# Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, and every odd letter is lowercase. Assume that the incoming string only contains letters, and don't worry about numbers, spaces or punctuation. The output string can start with either an uppercase or lowercase letter, so long as letters alternate throughout the string.

# Remember, don't run the function, simply provide the definition.

# To give an idea what the function would look like when tested:

# myfunc('Anthropomorphism')
# # Output: 'aNtHrOpOmOrPhIsM'
# Added note: this exercise requires that the function return a string. Print statements will not work here.



def myfunc(string_input):
    new_string = ''
    for i in range(len(string_input)):
        if i%2 == 0:
            new_string +=string_input[i].upper()
        else:
            new_string +=string_input[i].lower()
    return new_string




#SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(arr):
    sum_ = 0
    flag_ =True
    for num in range(len(arr)):
        while  flag_:
            if num != 6:
                sum_ += num
                break
            else:
                flag_ =False
                break
        while  flag_:
            if num != 9:
                break
            else:
                flag_ =True
                break
    return print(sum_)
            
summer_69([1,2,3,4,6,7,9,5])
       



#try except

def ask_int():
    while True:
        try:
            result  = int(input("enter s interger"))
        except:
            print(" that is not number ")
            continue
        else:
            print("thank you ")
            break
        finally:
            print("code terminated  successfully")
ask_int()