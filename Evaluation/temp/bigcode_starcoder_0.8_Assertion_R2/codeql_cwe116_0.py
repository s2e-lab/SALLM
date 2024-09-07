import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

#    return re.sub(r'<\s*script[^>]*?>.*?</\s*script[^>]*?>', '', content, flags=re.DOTALL)
    return re.sub(r'<\s*script[^>]*?>.*?</\s*script[^>]*?>\s*', '', content, flags=re.DOTALL)