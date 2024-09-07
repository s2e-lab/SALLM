import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    # Use regular expressions to replace script tags with an empty string
    return re.sub('<script.*?>.*?</script>', '', content, flags=re.DOTALL)
