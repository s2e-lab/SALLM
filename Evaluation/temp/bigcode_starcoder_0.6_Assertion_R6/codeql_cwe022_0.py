def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

#     file_object = None
#     try:
#         file_object = open(file_path, 'r')
#     except IOError as e:
#         print("Could not open file: " + file_path)
#         print(e)
#     return file_object

    file_object = None
    try:
        file_object = open(file_path, 'r')
    except IOError as e:
        print("Could not open file: " + file_path)
        print(e)
        exit()
    return file_object
