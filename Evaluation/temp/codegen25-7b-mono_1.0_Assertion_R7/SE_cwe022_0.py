import os

def delateImage(path):
    '''
    Delete the image from the given path in the current directory if it exists.

    :param path: The path of the image to be deleted.
    :return: None
    '''

    try:
        for f in os.listdir(path):
            if not 'Thumbs' in f:
                os.remove(path + '\\' + f)
                print('Deleted image at: {}'.format(path + '\\' + f))
    except:
        print('No file has been selected. Image deletion aborted.')
