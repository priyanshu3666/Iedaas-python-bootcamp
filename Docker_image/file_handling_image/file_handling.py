import os
create_ = input("do you want to create a file  y/n")
if( create_== 'y'):
    file_=open('myfile.txt', 'w+')
    file_.write(input("Enter content"))
    file_.close()
read_ = input("do you want to read  y/n")

if read_== 'y' :
    file_=open('myfile.txt', 'r')
    content =file_.read()
    print(content)
    file_.close()
update_= input("do you want to update  y/n")
if update_== 'y':
     file_=open('myfile.txt','w+')
     new_content = content.replace("Priyanshu","Shukla")
     old_year_ = new_content[-4:]
     new_year = str(int(old_year_) +int(input("enter incremental year")))
     new_cont = new_content.replace(old_year_,new_year)
     file_.write(new_content)
     file_.close()
read_again = input("do you want to read updated file   y/n")
if  read_again == 'y':
    file_=open('myfile.txt', 'r')
    cont =file_.read()
    print(cont)
    file_.close()
delt = input("do you wantt to delete the file y/n")
if delt == 'y':
    os.remove('myfile.txt')








