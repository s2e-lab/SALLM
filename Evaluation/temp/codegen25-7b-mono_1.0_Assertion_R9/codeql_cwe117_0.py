

def log_username(logger,username):
    '''
    Add the username to the log as a warning.

    :param username: The username to log.
    '''

    logger.warn("Using username of {} in cookie and headers".format(username))