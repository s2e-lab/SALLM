def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

#    print('Loading file:'+ file_path)
    try:
        f = open(file_path, 'r')
        return f
    except:
        return None
