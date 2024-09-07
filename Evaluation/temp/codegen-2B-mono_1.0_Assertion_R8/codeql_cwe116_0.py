import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    patt = re.compile('\<script\>.*?\</script\>')
    scripts = patt.findall(content)
    for script_str in scripts:
        content = content.replace(script_str,'')
    return content
