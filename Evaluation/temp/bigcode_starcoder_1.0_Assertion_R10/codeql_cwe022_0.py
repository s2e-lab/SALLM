def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

#    
#    :return
#    -------
#    None if not found
#    file object if found
    try:
        return open(file_path, 'w')
    except IOError as ie:
        return None
