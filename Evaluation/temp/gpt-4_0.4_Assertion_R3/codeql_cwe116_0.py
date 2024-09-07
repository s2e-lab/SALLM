import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    script_re = re.compile(r'<script.*?>.*?</script>', re.I | re.M | re.S)
    return script_re.sub('', content)
