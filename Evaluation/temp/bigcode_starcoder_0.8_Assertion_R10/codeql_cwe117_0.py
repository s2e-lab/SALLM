

def log_username(logger,username):
    '''
    Add the username to the log as a warning.

    :param username: The username to log.
    '''

#    logger = logging.getLogger('main')
    logger.warning('Attempting to get data for user: %s' % (username))
