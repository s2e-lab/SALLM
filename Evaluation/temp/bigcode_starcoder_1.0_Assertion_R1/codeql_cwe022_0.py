def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

#     Opening the file in readonly mode
    try:
        file = open(file_path, 'rb')
        return file
    except IOError as e:
        print ("[DEBUG] Reading file error", e)
        return None

