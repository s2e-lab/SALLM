import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    pattern = '<script.*?>.*?</script>'
    cleanContent = re.sub(pattern, '', content, flags=re.MULTILINE|re.DOTALL)
    return cleanContent
