def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    print('\033[1;32mFile'+ file_path +'successfully opened.\033[0m')
    return open(file_path, 'r')

