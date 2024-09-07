

def log_username(logger,username):
    '''
    Add the username to the log as a warning.

    :param username: The username to log.
    '''

#TODO add an option for logging to file system
    logger.warning(username)

