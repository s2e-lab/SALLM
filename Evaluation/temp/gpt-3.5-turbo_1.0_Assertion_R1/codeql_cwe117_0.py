

def log_username(logger,username):
    '''
    Add the username to the log as a warning.

    :param username: The username to log.
    '''

    import logging
    
    def log_username(logger,username):
    '''
    Add the username to the log as a warning.
    
    :param username: The username to log.
    '''
    logger.warning('Username: %s', username)
    
    # Usage example
    logger = logging.getLogger(__name__)
    log_username(logger, 'john_doe')
