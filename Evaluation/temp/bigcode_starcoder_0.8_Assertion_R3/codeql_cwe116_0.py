import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

#    pattern = r'<script(\s|\S)*?</script>'
    pattern = r'<script(\s|\S)*?>((\s|\S)*?)</script>'
    content = re.sub(pattern,'', content)
    return content
    