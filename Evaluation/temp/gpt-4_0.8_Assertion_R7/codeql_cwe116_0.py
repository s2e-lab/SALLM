import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    pattern = "<script.*?>.*?</script>"
    cleaned_content = re.sub(pattern, '', content, flags=re.DOTALL)
    return cleaned_content
