import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

#     pattern = re.compile(r'<script.*?</script>', re.DOTALL)
    pattern = re.compile(r'<script.*?>.*?</script>', re.DOTALL)
    return pattern.sub('', content)
