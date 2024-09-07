def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    try:
        file = open(file_path, 'r')
    except FileNotFoundError:
        print('File does not exist.')
        return None
    except PermissionError:
        print('Permission denied.')
        return None
    except OSError:
        print('OS error.')
        return None
    except:
        print('Unknown error.')
        return None
    return file
