def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    
    # check if file exists at given path and if not, exit the program
    if not os.path.isfile(file_path):
        sys.exit('ERROR: file \'%s\' cannot be opened.' % file_path)
    return open(file_path, 'r')
    
