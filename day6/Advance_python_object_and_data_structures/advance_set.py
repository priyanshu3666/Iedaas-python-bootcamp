# s =set()
# s.add(1)
# s.add(2)
# s.clear()
# s = {1,2,3}
# sc = s.copy()
# s.add(4) 
# s.difference(sc)
# s1={1,2,3,4,5}
# s2 ={1,2,3}
# s1.difference_update(s2)
# s.discard(2)
# s1.intersection(s2)
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}
# s1.isdisjoint(s2)

# s1.isdisjoint(s3)
# s1.issubset(s2)

# s2.issuperset(s1)

# s1.issuperset(s2)
print(s1.symmetric_difference(s2))
print(s1.union(s2))
s1.update(s2)
print(s1)