from jaanca_utils_os import EnvironmentParserLoader, FileFolderManagement
from prettytable import PrettyTable

class Environment:
    HOST = "ENGINE_POSTGRES_CONN_HOST"
    DB_NAME = "ENGINE_POSTGRES_CONN_DB"
    PASSWORD = "ENGINE_POSTGRES_CONN_PASSWORD"
    PORT = "ENGINE_POSTGRES_CONN_PORT"
    USER = "ENGINE_POSTGRES_CONN_USER"
    SSL = "ENGINE_POSTGRES_CONN_SSL"
    FLOAT = "FLOAT"
    LIST = "LIST"
    DICT = "DICT"
    BOOL_TRUE = "BOOL_TRUE"
    BOOL_TRUE_ONE = "BOOL_TRUE_ONE"
    BOOL_TRUE_TWO = "BOOL_TRUE_TWO"
    BOOL_FALSE_ONE = "BOOL_FALSE_ONE"
    BOOL_FALSE_TWO = "BOOL_FALSE_TWO"
    BOOL_FALSE_INCORRECT = "BOOL_FALSE_INCORRECT"
    NO_DATA_TUPLE = ("VARIABLE","Not Exist")
    NO_DATA_LIST = ["VARIABLE","Not Exist"]
    NO_DATA_BOOL = ["VARIABLE","1"]

# Load varibles from current folder
env_full_path = FileFolderManagement.build_full_path_from_current_folder(__file__,filename=".env")
# Load varibles from current folder and subfolders
# env_full_path = FileFolderManagement.build_full_path_from_current_folder(__file__,filename=".env",folder_list=["folder2"])
# Load varibles from disk path: c:\tmp
# env_full_path = FileFolderManagement.build_full_path_to_file("c:",file_name=".env",folder_list=["tmp"])

settings = EnvironmentParserLoader(Environment,env_full_path=env_full_path)

def print_attributes(cls):
    columns = ["Name", "Type", "Value"]
    myTable = PrettyTable(columns)
    for attribute_name, attribute_value in vars(cls).items():
        attribute_type = type(attribute_value)
        myTable.add_row([attribute_name, attribute_type.__name__, attribute_value])
    print(myTable)        

print_attributes(settings)

