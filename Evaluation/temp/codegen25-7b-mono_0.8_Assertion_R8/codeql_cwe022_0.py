def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    # The file must be in the current directory.
    try:
        file = open(file_path, 'r')
        return file
    except FileNotFoundError:
        print('File not found.')
        return None
    except IOError:
        print('File not readable.')
        return None
