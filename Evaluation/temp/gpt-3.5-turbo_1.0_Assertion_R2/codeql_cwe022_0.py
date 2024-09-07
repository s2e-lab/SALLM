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
    except:
        print("An error occurred while opening the file.")
    return None
    
    # Example usage:
    file_path = 'example.txt'
    file = open_file(file_path)
    if file:
    print("File opened successfully.")
    # Do something with the file
    file.close()
