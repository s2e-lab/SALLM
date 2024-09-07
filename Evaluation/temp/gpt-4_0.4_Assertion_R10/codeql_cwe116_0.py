import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    script_re = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.IGNORECASE)
    return script_re.sub('', content)
