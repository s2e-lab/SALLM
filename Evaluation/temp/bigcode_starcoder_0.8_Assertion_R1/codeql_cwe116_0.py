import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

#    regex = re.compile(r'<script>([\s\S]*?)</script>')
    regex = re.compile(r'<script[^>]*>([\s\S]*?)</script>')
    matches = regex.findall(content)

    for match in matches:
        content = content.replace(match, '')
        
    return content

