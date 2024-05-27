from jaanca_utils_os import FileFolderManagement

# root path
path=FileFolderManagement.build_full_path_from_current_folder(__file__,filename="filename.txt")
print(f"Full path from current folder: {path}")

# subfolders path from current folder
folder_list = ["folder1", "folder2"]
path=FileFolderManagement.build_full_path_from_current_folder(__file__,folder_list=folder_list,filename="filename.txt")
print(f"Full path from current folder: {path}")