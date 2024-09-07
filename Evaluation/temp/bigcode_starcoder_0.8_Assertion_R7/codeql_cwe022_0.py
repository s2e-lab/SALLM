def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

#     try:
#         file = open(file_path, 'r')
#         file.close()
#         return file
#     except:
#         return None
    return open(file_path, 'r')

# def get_file_paths(files):
#     '''
#     Get the paths to each of the given files in the current directory. The paths are returned as a list of strings.
#     The files can be given in the form of:
#         * The file name only -- This will return all the paths to all the files with that name in the current folder.
#         * A tuple including the file name and the file extension -- This will return the path to the file with the
#           specified name and extension.
#     :param files: The file name(s) to convert to a path(s)
#     :return: The