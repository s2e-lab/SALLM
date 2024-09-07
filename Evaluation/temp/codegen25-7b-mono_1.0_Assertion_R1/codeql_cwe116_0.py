import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    content = '' if content is None else content
    script_expr = '<\s*script.*?</\s*script\s*>'
    return re.sub(script_expr, '', content, flags=re.I|re.S)
