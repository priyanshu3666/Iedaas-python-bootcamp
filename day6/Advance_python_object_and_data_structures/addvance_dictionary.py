dict_={x:x**2 for x in range(10)}
print(dict_)
dict_ = {'k1':1,'k2':2}
for k in dict_.keys():
    print(k)

for v in dict_.values():
    print(v)

for item in dict_.items():
    print(item)

key_view = dict_.keys()
print(key_view)
dict_['k3'] = 3
print(dict_)
print(key_view)
