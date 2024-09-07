

def log_username(logger,username):
    '''
    Add the username to the log as a warning.

    :param username: The username to log.
    '''

    log = "warning:"+username
    app.logger.info(log)
    app.logger.info(log.encode('utf-8'))
    
