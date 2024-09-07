import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

#    regex = re.compile('<script\s*[^\>]*>[\s\S]*?</script>')  
    regex = re.compile('<\s*script\s*[^\>]*[\s\S]*?>.*<\s*/\s*script\s*>')
    filtered = regex.sub(filter_script_tags, content)
    return filtered
    