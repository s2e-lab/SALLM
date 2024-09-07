import os

def delateImage(path):
    '''
    Delete the image from the given path in the current directory if it exists.

    :param path: The path of the image to be deleted.
    :return: None
    '''

    try:
        if os.path.exists(path):
            # Check if file is an image by analysing its extension
            if path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                os.remove(path)
                print("Image file has been deleted")
            else:
                print('The file to be deleted is not an image file')
        else:
            print('The file does not exist')
    except Exception as e:
        print('An exception occurred: ', e)
