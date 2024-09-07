import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    # Define regex pattern
    scriptPattern = re.compile('<script.*?>.*?</script>', re.DOTALL | re.IGNORECASE)
    # Replace script tags with empty string
    cleanedContent = re.sub(scriptPattern, '', content)
    return cleanedContent
