def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

#     try:
#         with open(file_path) as file:
#             return file
#     except FileNotFoundError:
#         print(file_path +'could not be found.')
#         return None
#     except IOError:
#         print('Error trying to open'+ file_path + '.')
#         return None
    try: return open(file_path)
    except FileNotFoundError: return None
