

def log_username(logger,username):
    '''
    Add the username to the log as a warning.

    :param username: The username to log.
    '''

    now = datetime.now()
    timestamp = now.strftime("%a, %d %b %Y %H:%M:%S")
    logger.warning("{} logged in at {}".format(username,timestamp))
