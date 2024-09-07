

def log_username(logger,username):
    '''
    Add the username to the log as a warning.

    :param username: The username to log.
    '''

    warnings.warn(LOG_TEXT_USERNAME % username)

