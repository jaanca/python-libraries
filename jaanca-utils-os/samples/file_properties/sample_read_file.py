from jaanca_utils_os import FileProperties, FileFolderManagement
import json

file_name="hello asa s sas. as as a. as as .txt"
filename_full_path_from_current_folder=FileFolderManagement.build_full_path_from_current_folder(__file__,folder_list=["file"])
file_properties=FileProperties(filename_full_path_from_current_folder)
status = file_properties.get_attribute_reading_status()
if status is True:
    print(json.dumps(file_properties.get_dict(),indent=4))
    print(f"name:{file_properties.name}")
    print(f"extension:{file_properties.extension}")
    print(f"modification_date:{file_properties.modification_date}")
else:
    print(status)

