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
        print(f"File {file_path} not found.")
        return None
    except IOError:
        print(f"Error occurred trying to read the file {file_path}.")
        return None
    except Exception as e:
        print(f"Unexpected error occurred while trying to read the file {file_path}. Error message: {str(e)}")
        return None
