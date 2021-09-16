import re
list_of_index_ = []
text = 'this is a string for regex, purpose only. regex '
pattern = 'regex'
match = re.findall(pattern,text)
print(match)
for match in re.finditer(pattern,text):
    list_of_index_.append(match.span())

print(list_of_index_)
