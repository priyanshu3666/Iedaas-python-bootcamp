import re
email_pattern = r'\w+.\w+@\w+[.]\w+'
phone_pattern = r'\d{10}'
text = 'priyanshu shukla priyanshu.shukla@gmail.com 8004954515'
email_pattern_compile = re.compile(email_pattern)
phone_pattern_compile = re.compile(phone_pattern)
result  = email_pattern_compile.search(text)
result1 = phone_pattern_compile.search(text)
print(result.group())
print(result1.group())

