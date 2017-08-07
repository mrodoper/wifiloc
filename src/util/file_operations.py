import os

TMP_FOLDER = "tmp"
RESULTS_FOLDER = "results"

def create_folder(directory):
    """Function to create a directory

    @param: directory Name of the directory to create in string form

    """
    if isinstance(directory, str):
        if not os.path.exists(directory):
            os.makedirs(directory)
        return True
    return False

def create_tmp_folder():
    """Function to create the tmp folder inside the project"""
    create_folder(TMP_FOLDER)

def create_results_folder():
    """Function to create the tmp folder inside the project"""
    create_folder(RESULTS_FOLDER)

def read_file(file_path):
    """Function to read the contents of a file to a var"""
    try:
        with open(file_path, "r") as file:
            content = file.read()
    except IOError as e:
        print("File at " + file_path +" does not exist")
        content = None
    return content
