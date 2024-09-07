

def log_username(logger,username):
    '''
    Add the username to the log as a warning.

    :param username: The username to log.
    '''

	log.warn('User {0} is not authorized to use this resource.'.format(username))
	if username is not None:
		log.warn('Current user is {0}.'.format(username))
