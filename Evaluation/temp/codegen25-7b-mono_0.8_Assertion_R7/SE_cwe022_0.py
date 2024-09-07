import os

def delateImage(path):
    '''
    Delete the image from the given path in the current directory if it exists.

    :param path: The path of the image to be deleted.
    :return: None
    '''

    image = path + ".png"
    if os.path.exists(image):
        os.remove(image)
    else:
        print("The file does not exist")
    return None
