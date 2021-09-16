import time
import timeit

def function1(num):
    list_ =[x for x in range(num)]
 
def function2(num):
    list_1 = list(map(int,range(num)))
  
start_time =time.time()
function1(100)
end_time = time.time()
elapsed_time = end_time - start_time
print(f'the exectuoin time for function1 is {elapsed_time}') 
    
start_time1 =time.time()
function1(100)
end_time1 = time.time()
elapsed_time1 = end_time1 - start_time1
print(f'the exectuoin time for function2 is {elapsed_time1}') 

stmt1 = '''
function1(100)
'''
setup1 = '''
def function1(num):
    list_ =[str(x) for x in range(num)]
'''

stmt2 = '''
function2(100)
'''
setup2 = '''
def function2(num):
    list_1 = list(map(str,range(num)))
'''
print()
print(timeit.timeit(stmt1,setup1,number =100000))
print()
print(timeit.timeit(stmt2,setup2,number =100000))