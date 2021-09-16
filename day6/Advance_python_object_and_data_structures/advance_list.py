list1 = [1,2,3]
list1.append(4)
list1.count(2)
x = [1, 2, 3]
x.append([4, 5])
print(x)
x = [1, 2, 3]
x.extend([4, 5])
print(x)
list1.index(2)
list1.insert(2,'inserted')
ele  = list1.pop(1)
print(ele)
print(list1)
list1.remove('inserted')
list2 = [1,2,3,4,3]
list2.remove(3)

list2.reverse()
list2.sort()
list2.sort(reverse=True)
