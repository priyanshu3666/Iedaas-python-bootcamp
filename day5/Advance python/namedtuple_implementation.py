from collections import namedtuple

book = namedtuple('book',['title','author','year',])
new_book = book('physics','H.C. Verma','2010')
list_ = [new_book.title,new_book.author]
list_1= [new_book[0],new_book[1]]

print(list_)
print()
print(list_1)
