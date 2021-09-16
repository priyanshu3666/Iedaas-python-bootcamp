import os
import shutil
file_ =open("practice.txt","w+")
file_.write("i am writing a string inside practice.txt file ")
file_.close()

print(os.getcwd())
print(os.listdir("/home/priyanshu/Desktop/Iedaaas-python-bootcamp"))
# shutil.move("practice.txt","/home/priyanshu/Desktop/Iedaaas-python-bootcamp/day5/Advance python")
file_path ="/home/priyanshu/Desktop/Iedaaas-python-bootcamp/day5"

for folder,sub_folder,files in os.walk(file_path):
    print(f"currently looking at {folder}")
    print()
    print("the sub folders are :")
    for sub_folder in sub_folder:
        print(f"\t subfolder :{sub_folder}")

    print()
    print("the files are ")
    for files_ in files:
        print(f'\t file : {files_}')
    print()