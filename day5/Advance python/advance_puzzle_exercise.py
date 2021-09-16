import shutil
import os
import re
#shutil.unpack_archive('unzip_me_for_instructions.zip','extracted_puzzle_file','zip')
print(os.getcwd())
with open('extracted_puzzle_file/extracted_content/Instructions.txt') as file_handler:
    contents = file_handler.read()
    print(contents)
phone_pattern =r'\d{3}-\d{3}-\d{4}'

def seach_pattern(file,phone_pattern =r'\d{3}-\d{3}-\d{4}'):
    file_handler = open(file,'r')
    text = file_handler.read()
    if  re.search(phone_pattern,text):
        return re.search(phone_pattern,text)
    else:
        return ''

searched_fetch_dir =[]

for folder,sub_folder,files in os.walk(os.getcwd()+'/extracted_puzzle_file/extracted_content'):
    for file in files:
        full_directory_path = folder+'/'+ file

        searched_fetch_dir.append(seach_pattern(full_directory_path))

for result in searched_fetch_dir:
    if result != '':
        print(result.group())
