def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    try:
        file_object = open(file_path)
        return file_object
    except IOError as e:
        print("Couldn't open \"{0}\"".format(file_path))
        print(e)
        exit(-1)

