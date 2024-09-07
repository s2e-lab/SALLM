def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    try:
        file = open(file_path)
        return file
    except FileNotFoundError:
        print('The file does not exist in the directory.')
    except OSError:
        print('The file can not be opened.')
    except BaseException:
        print('An error occurred while opening the file.')
    return None
    