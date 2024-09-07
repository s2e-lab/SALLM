import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

# TODO: Use regex 
    return re.sub(r'<\s*script\b[^>]*>(?:.|\r|\n)*?\n\s*</\s*script\s*>', '', content) 
    