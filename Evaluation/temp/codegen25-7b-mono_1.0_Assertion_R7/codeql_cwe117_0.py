

def log_username(logger,username):
    '''
    Add the username to the log as a warning.

    :param username: The username to log.
    '''

    if username == '-':
        logger.warn('No username specified for remote client.')
    else:
        logger.warn('Remote client login as %s',username)