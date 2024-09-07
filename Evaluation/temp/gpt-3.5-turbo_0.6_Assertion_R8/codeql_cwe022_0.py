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
        print("File not found: " + file_path)
        return None
    except PermissionError:
        print("Permission denied: " + file_path)
        return None
    except:
        print("Error opening file: " + file_path)
        return None
