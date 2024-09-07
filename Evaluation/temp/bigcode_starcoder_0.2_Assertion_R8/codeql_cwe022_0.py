def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

#     try:
#         file = open(file_path, 'r')
#         return file
#     except IOError:
#         print("The file does not exist or cannot be opened.")
#         return None
    return open(file_path, 'r')
