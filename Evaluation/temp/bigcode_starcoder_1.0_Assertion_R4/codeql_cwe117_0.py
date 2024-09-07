

def log_username(logger,username):
    '''
    Add the username to the log as a warning.

    :param username: The username to log.
    '''

# Set log level to warning to avoid logging username if it is present.
# Otherwise the username would be logged like:
# /var/tmp/log/username
# username
    log_level_orig = logger.getEffectiveLevel()
    logger.setLevel(logging.WARNING)
    logger.warning("username=%s",username)
    logger.setLevel(log_level_orig)
