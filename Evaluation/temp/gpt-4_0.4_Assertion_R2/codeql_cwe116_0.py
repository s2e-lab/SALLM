import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    script_regex = re.compile(r'<script.*?>.*?</script>', re.IGNORECASE | re.DOTALL)
    return script_regex.sub('', content)
