import zipfile 
file_handler = open("file1.txt",'w+')
file_handler.write(" this is file 1 ")
file_handler.close()

file_handler = open("file2.txt",'w+')
file_handler.write(" this is file 2 ")
file_handler.close()
compress_file = zipfile.ZipFile("compress_file.zip",'w')
compress_file.write('file1.txt',compress_type=zipfile.ZIP_DEFLATED)
compress_file.write('file2.txt',compress_type=zipfile.ZIP_DEFLATED)
compress_file.close()

zip_obj = zipfile.ZipFile("compress_file.zip",'r')
zip_obj.extractall("extracted_content")

