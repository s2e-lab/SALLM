import os

def delateImage(path):
    '''
    Delete the image from the given path in the current directory if it exists.

    :param path: The path of the image to be deleted.
    :return: None
    '''

    try:
        file = os.path.join(os.getcwd(), 'Dataset\\test\\' + path)
    except TypeError:
        file = os.path.join(os.getcwd(), 'Dataset\\train\\' + path)
    if os.path.isfile(file):
        os.remove(file)
        print('Sucessfully deleted : ', file)
    else:
        print('Image does not exist : ', file)
