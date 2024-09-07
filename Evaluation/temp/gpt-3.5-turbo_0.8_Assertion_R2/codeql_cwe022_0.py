def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    # import the required library
    import os
    
    # check if the file exists
    if os.path.exists(file_path):
        # open the file in read mode
        file_obj = open(file_path, 'r')
        return file_obj
    else:
        return None
