from jaanca_utils_os import FileFolderManagement

# Write file to current folder
file_name="hello.txt"
current_folder=FileFolderManagement.build_full_path_from_current_folder(__file__)
folders=FileFolderManagement.get_folder_list(current_folder)
file_name_full_path = FileFolderManagement.build_full_path_to_file("c:",file_name,folders)
text = """Hello world !
Hello world !"""
status,error_msg=FileFolderManagement(file_name_full_path).write_to_disk(text)
if(status):
    print("file created successfully: "+file_name_full_path)
else:
    print("error:" + error_msg)

# Write file in root path
file_name="hello.txt"
file_name_full_path = FileFolderManagement.build_full_path_to_file("c:",file_name)
text = """Hello world !
Hello world !"""
status,error_msg=FileFolderManagement(file_name_full_path).write_to_disk(text)
if(status):
    print("file created successfully: "+file_name_full_path)
else:
    print("error:" + error_msg)
