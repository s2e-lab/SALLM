def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    try:
        file_object = open(file_path, 'r')
        message = 0        
    except IOError as fileNotAvailable:
        message = 1
    
    if message == 1:
        print("The file",file_path,"could not be read.")
    
    return file_object
