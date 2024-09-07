def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

#     try:
#         f = open(file_path, "r", encoding="utf-8")
#     except:
#         print("Error: Couldn't open file", file_path)
#         return None
    f = open(file_path, "r", encoding="utf-8")
    return f
