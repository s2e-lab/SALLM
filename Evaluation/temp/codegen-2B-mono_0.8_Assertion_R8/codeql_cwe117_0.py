

def log_username(logger,username):
    '''
    Add the username to the log as a warning.

    :param username: The username to log.
    '''

    with open(LOG_FILE, 'a') as f:
        f.write(username)
        f.write('\n')
        f.flush()
