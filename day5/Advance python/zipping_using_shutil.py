import shutil
dir_to_zip = "/home/priyanshu/Desktop/Iedaaas-python-bootcamp/extracted_content"
output_foldername = "example"
shutil.make_archive(output_foldername,"zip",dir_to_zip)
shutil.unpack_archive('example.zip','example_unzip','zip')