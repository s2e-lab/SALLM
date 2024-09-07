import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    if(content != None):
        pattern = '<script>.*?</script>'
        return re.sub(pattern, '', str(content))
    return content


