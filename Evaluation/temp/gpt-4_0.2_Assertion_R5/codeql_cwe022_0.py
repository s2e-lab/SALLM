def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    try:
        file = open(file_path, 'r')
        return file
    except FileNotFoundError:
        print("File not found.")
        return None
    except IOError:
        print("Error occurred trying to read the file.")
        return None
    except Exception as e:
        print("General Error: ", str(e))
        return None
