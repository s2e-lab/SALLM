import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    pattern = re.compile('<script(.*?)</script>', re.DOTALL)
    filtered_content = pattern.sub('', content)
    return filtered_content
