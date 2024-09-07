def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    try:
        input_file = open(file_path, 'rb')
        return input_file
    except Exception as e:
        log(e)
        return None
