'''
THis code is wwritten by priyanshu Shukla regarding implementation of custom exceptions in python 
'''
class DemoException(Exception):
    def __init__(self, message):
        super().__init__(message)
        
class NumberFormatException(Exception):
    def __init__(self, message, value):
        message = f'{value} is not a number'
        super().__init__(message)
        
message = "Exception occured."

def triggerException(num):
    if (not num.isdigit()):
        raise NumberFormatException(message, num)
    elif (num == 0):
        raise DemoException(message)
    else:
        print(num)

num = "sample string"
try:
    triggerException(num)
    print("Code has successfully been executed.")
except DemoException:
    print("Error: Number should not be 0.")
except NumberFormatException:
    print(num+" is not a number.")
finally:
    print(" code terminates smoothly")