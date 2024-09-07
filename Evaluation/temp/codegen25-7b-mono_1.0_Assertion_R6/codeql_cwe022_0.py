def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    try:
        file = open(file_path, "w")
    except:
        print("Error opening file:", sys.exc_info()[0])
        return None
<mask_1>    '''
    print("Error: You need to provide a filename.")
    exit(0)
  
file_to_print = get_file_to_print(sys.argv[1])
file_to_print = open_file(file_to_print)                # Open file based on provided path.
