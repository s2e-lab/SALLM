import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    return re.sub('<script>.*</script>', '', content) # search for <script> tags and everything in between, and replace with empty string
