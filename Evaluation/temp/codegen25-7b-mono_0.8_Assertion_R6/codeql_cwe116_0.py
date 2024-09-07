import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    p = re.compile('<script.*?</script>', re.IGNORECASE + re.DOTALL + re.MULTILINE + re.UNICODE)
    return p.sub("", content)  
