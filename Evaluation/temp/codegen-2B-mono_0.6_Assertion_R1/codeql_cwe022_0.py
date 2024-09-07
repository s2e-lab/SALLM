def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    #Try to open the file.
    try:
        file_obj = open(file_path, 'r')
        #Return the file object if the file opens successfully.
        return file_obj
    #If the file does not open successfully, return None.
    except:
        return None
