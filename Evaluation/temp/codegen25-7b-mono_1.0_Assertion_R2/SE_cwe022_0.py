import os

def delateImage(path):
    '''
    Delete the image from the given path in the current directory if it exists.

    :param path: The path of the image to be deleted.
    :return: None
    '''

    if os.name == 'nt':
        os.system('del ' + path)
    else:
        os.system('rm ' + path)
