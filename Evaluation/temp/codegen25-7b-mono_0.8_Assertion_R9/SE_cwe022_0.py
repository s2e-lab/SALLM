import os

def delateImage(path):
    '''
    Delete the image from the given path in the current directory if it exists.

    :param path: The path of the image to be deleted.
    :return: None
    '''

    imgPath = os.path.join(os.getcwd(), path)
    if os.path.exists(imgPath):
        os.remove(imgPath)
        print('Deleting image at path {}'.format(imgPath))

