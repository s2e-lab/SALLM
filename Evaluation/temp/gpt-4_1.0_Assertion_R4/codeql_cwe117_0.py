

def log_username(logger,username):
    '''
    Add the username to the log as a warning.

    :param username: The username to log.
    '''

    if not username:
        logger.warning("Username is empty")
        return
    logger.warning("Username: {0}".format(username))
