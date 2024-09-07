import os

def delateImage(path):
    '''
    Delete the image from the given path in the current directory if it exists.

    :param path: The path of the image to be deleted.
    :return: None
    '''

    if not os.path.exists(path):
        return
    
    if os.path.isdir(path): # If it'a a directory
        for f in os.listdir(path):
            delateImage(f)
        try:
            os.rmdir(path)
        except:
            pass
    else:<mask_1> is deleted.
    
    path: str,
    '''
    if not os.path.exists(destPath):
        os.makedirs(destPath)
    
    if os.path.isdir(path):<mask_2><sep><mask_1>
        try:
            os.remove(path)
        except:
            pass
