def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

#    try:
    if os.path.exists(file_path):
        return open(file_path)
    else:
        print("Error. Given file not exists!")
        return None
#    except IOError:
#        print("Error! Check if file exists in the given file path.")

