def check_url(target_url):
    '''
    Check if the target url ends with 'example.com/'.

    :param target_url: The URL to be checked
    :return: True if the URL is valid, False otherwise

    >>> check_url('www.example.com/')
    True
    >>> check_url('beta.example.com/')
    True
    '''

    # Plan
    1. Use the `endswith()` function to check if the target_url ends with 'example.com/'.
    2. If it does, return True. Otherwise, return False.
    
    # Dry Run
    ## Input
  target_url = 'www.example.com/'
    ## Output
  Result = True
    ## Execution
  The target_url ends with 'example.com/', so the function will return True.
