def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

#     print(file_path)
    try:
        file = open(file_path, 'r')
        return file
    except IOError:
        print("File not found. Please check the file path.")
        return None
