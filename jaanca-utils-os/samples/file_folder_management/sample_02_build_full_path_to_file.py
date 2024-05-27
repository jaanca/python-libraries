from jaanca_utils_os import FileFolderManagement

# root path
file_name = "hello.txt"
file_name_full_path = FileFolderManagement.build_full_path_to_file("c:",file_name)
file_name_full_path_without_file_name = FileFolderManagement.build_full_path_to_file("c:",file_name='')
print(f"file_name_full_path={file_name_full_path}")
print(f"file_name_full_path_without_file_name={file_name_full_path_without_file_name}")

# subfolders path
file_name = "hello.txt"
folder_list = ["folder1", "folder2"]
file_name_full_path = FileFolderManagement.build_full_path_to_file("c:",file_name,folder_list)
file_name_full_path_without_file_name = FileFolderManagement.build_full_path_to_file("c:",file_name='',folder_list=folder_list)
print(f"file_name_full_path={file_name_full_path}")
print(f"file_name_full_path_without_file_name={file_name_full_path_without_file_name}")