import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    # Use regular expresion to find and replace <script> tags
    clean_content = re.sub('<script[^>]*?>.*?</script>', '', content, flags=re.DOTALL)
    
    return clean_content
