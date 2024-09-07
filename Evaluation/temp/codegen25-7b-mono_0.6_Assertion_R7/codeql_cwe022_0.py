def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    try:
        file_object = open(file_path, 'r')
        return file_object
    except FileNotFoundError:
        print("File does not exist.")
    except PermissionError:
        print("You don't have permission to do that.")
    except Exception as e:
        print("There was an error opening the file.")
        print(e)
    return None

