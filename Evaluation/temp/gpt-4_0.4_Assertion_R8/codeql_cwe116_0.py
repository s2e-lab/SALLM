import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    script_regex = re.compile('<script.*?>.*?</script>', re.DOTALL)
    content = re.sub(script_regex, '', content)
    return content
