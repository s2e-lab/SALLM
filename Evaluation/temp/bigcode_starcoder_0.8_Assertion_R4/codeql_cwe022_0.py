def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

#     print(file_path)
#     print(os.path.exists(file_path))
#     print(os.path.isfile(file_path))
    if(os.path.exists(file_path) and os.path.isfile(file_path)):
        try:
            file = open(file_path, 'r')
#             print(file.name)
            return file
        except:
            print("Error opening file " + file_path)
            return None
    else:
        print('\nNo such file.\n')
        return None
    