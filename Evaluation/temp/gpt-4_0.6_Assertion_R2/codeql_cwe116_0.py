import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    # Using regular expression to remove script tags
    return re.sub(r'<script[^>]*?>.*?</script>', '', content, flags=re.DOTALL)
