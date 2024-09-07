def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

#     file_path = file_path.replace(' ', '\\ ')
#     file_path = file_path.replace('/', '\\ ')
    try:
        fd = open(file_path, mode='r')
        return fd
    except:
        return None
