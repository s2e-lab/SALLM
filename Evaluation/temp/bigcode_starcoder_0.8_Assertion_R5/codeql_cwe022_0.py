def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

#     if not os.path.isfile(file_path):
#         return None
#     try:
#         file_stream = open(file_path, "r")
#     except:
#         return None
#     if not file_stream:
#         return None
    try:
        file_stream = open(file_path, "r")
        return file_stream
    except:
        return None


# In[8]:

