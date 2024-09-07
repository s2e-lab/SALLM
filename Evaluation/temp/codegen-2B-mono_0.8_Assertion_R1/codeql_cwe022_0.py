def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    try:
        with open(file_path) as f:
            pass
        return f
    except FileNotFoundError:
        return None
    except OSError as e:
        print(e)
        return None
