

def log_username(logger,username):
    '''
    Add the username to the log as a warning.

    :param username: The username to log.
    '''

#    if username!="null" and username!="undefined" and username!="":
    logger.warning("Username: "+username)
