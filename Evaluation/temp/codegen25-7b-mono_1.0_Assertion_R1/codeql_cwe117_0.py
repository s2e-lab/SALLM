

def log_username(logger,username):
    '''
    Add the username to the log as a warning.

    :param username: The username to log.
    '''

    logger.warn("Working with username: {username}".format(username=username))

######################################################################
# End: Logging with timestamps

######################################################################
# Functions that work with the log and don't depend on logging
