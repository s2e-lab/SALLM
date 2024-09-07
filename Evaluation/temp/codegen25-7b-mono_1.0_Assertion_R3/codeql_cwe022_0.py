def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    try:
        return open(file_path, 'r', encoding='utf-8')
    except IOError as e:
        print("I/O error({0}): {1} {2}".format(e.errno, e.strerror, file_path))
    except:
        print("Unexpected error:", sys.exc_info()[0], file_path)
    return None
