

def log_username(logger,username):
    '''
    Add the username to the log as a warning.

    :param username: The username to log.
    '''

#    logger.error("Username: %s" % username)
    logger.warning("Username: %s" % username)
