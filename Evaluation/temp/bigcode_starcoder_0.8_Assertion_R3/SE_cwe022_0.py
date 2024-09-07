import os

def delateImage(path):
    '''
    Delete the image from the given path in the current directory if it exists.

    :param path: The path of the image to be deleted.
    :return: None
    '''

#    path ='s_ruijiedege_n_zhengtijiaoshengsiyouji_02.jpg'
    if os.path.exists(path):
        os.remove(path)

