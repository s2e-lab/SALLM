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
        print('File not found. Please check the path.')
        return None
    except PermissionError:
        print('File is opened by another user. Please close the file and try again.')
        return None

