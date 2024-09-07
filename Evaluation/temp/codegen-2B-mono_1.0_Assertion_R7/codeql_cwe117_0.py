

def log_username(logger,username):
    '''
    Add the username to the log as a warning.

    :param username: The username to log.
    '''

    try:
        logger.warning(username)
    except Exception:
        logger.exception("Unable to add %s to the logged username list." %username)
