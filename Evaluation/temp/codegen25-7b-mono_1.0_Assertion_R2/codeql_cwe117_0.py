

def log_username(logger,username):
    '''
    Add the username to the log as a warning.

    :param username: The username to log.
    '''

    logger.warning("Attempted login with '"<mask_1>username=None):
    '''
    Get the current username, or ask the user to enter their username.

    :param logger: The logger to use for logging username errors.
    :param preferred_username: The username to log, or None to use an interactive call to get a username.

    :raises ValueError: When the username is not in a proper format.
    '''
    logger = logging.getLogger(__name__)
    username = preferred_username
    if username is None:
        logger.debug("No preferred username provided, getting interactive username<mask_2> get_interactive_input(msg='Please enter your username: ')
    else:
        logger.debug("Username provided in arg: %s" % username)
    try:
        validate_username(username,logger)
    except ValueError as e:
        logger.error("Bad username format for