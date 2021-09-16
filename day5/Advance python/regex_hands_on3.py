import re
text = 'the cat in the hat is splat .cat age is 7'
print(re.findall(r'cat|rat|hat',text)) #useing pipeline as or
print(re.findall(r'.at',text))
print(re.findall(r'^\w',text)) 
print(re.findall(r'\d$',text))

text2 = 'this sentence contains 4 sets .every set contains 67 elements'
print(re.findall(r'[^\d]+',text2))
text3 = 'hi! this sentence contains puntuations. so, we are going to remove it .but how?'
formatting_text = re.findall(r'[^!?.,]+',text3) 
new_formatted_string =''.join(formatting_text)
print(new_formatted_string)

text4 ='catpillar'
text5 ='catwalk'
text6 ='catclaw'
print(re.search(r'cat(claw|walk|pillar)',text4).group())
print(re.search(r'cat(claw|walk|pillar)',text5).group())
print(re.search(r'cat(claw|walk|pillar)',text6).group())