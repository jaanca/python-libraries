from jaanca_utils_os import EnvironmentParserLoader, FileFolderManagement
from prettytable import PrettyTable

''' Considerations on environmental variables
- An object must be specified with the variables that you want to create.
- The attributes of these objects will be loaded with the environment variables, according to the name assigned to them.
- If the attribute is mandatory, it will only be of type str and will contain the name of the environment variable to read.
- If the environment variable is optional or may not exist, the attribute must be of type tuple or list, where the first element is the environment variable to read and the second the default value to assign.

Example:
class Environment:
    ENV_VAR_NO_EXIT = ("VARIABLE","Not Exist")
    ENV_VAR_IS_MANDATORY = "VARIABLE"


'''

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

############
# select the location of the file to read
############

############
# Option 1
# Run the script from where the default environment variables .env file is located
# settings:Environment = EnvironmentParserLoader(Environment)

############
# Other Options
# Load varibles from current folder and subfolders
env_full_path = FileFolderManagement.build_full_path_from_current_folder(__file__,filename=".env",folder_list=["folder2"])
# Load varibles from disk path: c:\tmp
env_full_path = FileFolderManagement.build_full_path_to_file("c:",file_name=".env",folder_list=["tmp"])
# Load varibles from current folder
env_full_path = FileFolderManagement.build_full_path_from_current_folder(__file__,filename=".env")

settings:Environment = EnvironmentParserLoader(Environment,env_full_path=env_full_path)

def print_attributes(cls):
    columns = ["Name", "Type", "Value"]
    myTable = PrettyTable(columns)
    for attribute_name, attribute_value in vars(cls).items():
        attribute_type = type(attribute_value)
        myTable.add_row([attribute_name, attribute_type.__name__, attribute_value])
    print(myTable)        

print_attributes(settings)

print(f"settings.BOOL_FALSE_INCORRECT={settings.BOOL_FALSE_INCORRECT}")

