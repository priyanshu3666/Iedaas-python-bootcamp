import csv
data = open('example.csv',encoding = "utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)
for data in data_lines[:5]:
    print(data)
all_email = []
for column in data_lines[1:]:
    all_email.append(column[3])
full_name =[]
for name in data_lines[1:]:
    full_name.append(name[1] + " " + name[2])

file_to_output = open('to_save_file.csv',mode ='w',newline='')
csv_writer = csv.writer(file_to_output,delimiter = '\t')
csv_writer.writerow(['name','age','roll_no'])
csv_writer.writerows([['1','2','3'],['4','5','6']])
file_to_output.close()

f = open('to_save_file.csv',mode='a',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['1','2','3'])
f.close()