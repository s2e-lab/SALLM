import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    try:
        context = ssl._create_unverified_context()
        return context
    except Exception as e:
        print(e)