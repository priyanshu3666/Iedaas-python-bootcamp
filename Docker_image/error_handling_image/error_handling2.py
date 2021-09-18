
try:
    raise NameError("try block error ")  
except NameError:
    print (" Name errror handled")
    try:
        raise EOFError
    except:
        print("EOF error handled ")
    
finally:
    try:
        raise ImportError
    except :
        print(" Import Error handled")

    print("All goes fine ")