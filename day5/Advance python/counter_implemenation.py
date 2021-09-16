from collections  import Counter
mylist = [1,2,3,4,5,5,65,5.5]
mystring  = 'priyanshu shukla'
print(Counter(mystring))
print('')
print(Counter(mylist))
print(Counter(mylist).most_common(2))