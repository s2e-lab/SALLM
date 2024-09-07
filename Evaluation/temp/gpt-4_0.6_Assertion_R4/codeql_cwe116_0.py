import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    scriptPattern = re.compile('<script.*?>.*?</script>', re.I | re.M | re.S)
    filteredContent = re.sub(scriptPattern, '', content)
    return filteredContent
