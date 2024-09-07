import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    script_pattern = re.compile('<script.*?>.*?</script>', re.DOTALL)
    no_script_content = re.sub(script_pattern, '', content)
    return no_script_content
