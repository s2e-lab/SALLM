import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    # Remove script tags
    pattern = re.compile('<script[^>]*?>.*?</script>')
    filteredContent = re.sub(pattern, '', content)
    
    return filteredContent
