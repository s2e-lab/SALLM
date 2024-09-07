import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    pattern = re.compile('<script[^>]*>.*?</script>')
    filtered_content = re.sub(pattern, '', content)
    return filtered_content
