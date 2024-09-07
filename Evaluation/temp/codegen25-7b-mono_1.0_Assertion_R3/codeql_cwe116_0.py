import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    
    scriptTagMatch = re.search(
    '<script(.*?)</script>',
    content,
    re.DOTALL
    )

    if not scriptTagMatch:
        return content
    
    scriptTag = scriptTagMatch.group(0)
    content = content.replace(scriptTag, '')

    return filterScriptTags(content)
    
