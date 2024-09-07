import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    script_pattern = re.compile(r'<script.*?>.*?</script>', re.I | re.S)
    no_scripts = re.sub(script_pattern, '', content)
    return no_scripts
