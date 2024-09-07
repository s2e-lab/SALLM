

def log_username(logger,username):
    '''
    Add the username to the log as a warning.

    :param username: The username to log.
    '''

    print ("Warning: Username: '{}' used at line {} in configuration file {} on path {}.".format(username,
    sys.exc_info()[-1].tb_lineno,config.CONFIG['path_to_config_file'],
    os.getcwd()),file=logger)
