def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    try:
        return open(file_path, 'r')
    except Exception as e:
        print(f'Error occurred while trying to open the file: {e}')
        return None
