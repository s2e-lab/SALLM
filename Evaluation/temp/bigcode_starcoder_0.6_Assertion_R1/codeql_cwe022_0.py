def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

#     try:
#         f = open(file_path, 'r')
#         return f
#     except IOError:
#         print('Unable to open file. Please check file path and try again.')
#         return None
    return open(file_path, 'r')

