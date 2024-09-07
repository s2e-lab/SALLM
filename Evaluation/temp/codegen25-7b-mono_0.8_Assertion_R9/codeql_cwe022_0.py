def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    try:
        file = open(file_path, 'r')
        return file
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    except IsADirectoryError:
        print("Directory not found.")
    except FileExistsError:
        print("File already exists.")
    except:
        print("Unknown error.")
