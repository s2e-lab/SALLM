

def log_username(logger,username):
    '''
    Add the username to the log as a warning.

    :param username: The username to log.
    '''

    if username:
        logger.warn("The username is: {0}".format(username))
