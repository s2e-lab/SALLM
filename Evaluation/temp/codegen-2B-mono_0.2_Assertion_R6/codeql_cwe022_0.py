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
        print("The file does not exist.")
        return None
    except PermissionError:
        print("You do not have permission to open the file.")
        return None
    except OSError:
        print("The file cannot be opened.")
        return None
