import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

#    return re.sub('(?i)</?script.*?>','',content)
    return re.sub('(?i)<\s*script.*?>.*?</\s*script.*?>','',content,flags=re.MULTILINE|re.DOTALL)

