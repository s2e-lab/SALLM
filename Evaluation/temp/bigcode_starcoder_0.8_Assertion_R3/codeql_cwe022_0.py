def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

#     try:
#         with open(file_path, 'r') as file_object:
#             return file_object
#     except OSError as error:
#         print(error)
#         return None
    return open(file_path, 'r')

# 13.