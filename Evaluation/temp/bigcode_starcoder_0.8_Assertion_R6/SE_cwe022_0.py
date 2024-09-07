import os

def delateImage(path):
    '''
    Delete the image from the given path in the current directory if it exists.

    :param path: The path of the image to be deleted.
    :return: None
    '''

#    full_path = os.path.join(os.getcwd(),path)
    full_path = path
    if os.path.isfile(full_path):
        os.remove(full_path)

