import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    # Use the re module to remove script tags
    filtered_content = re.sub(r'<script>.*?</script>', '', content)
    return filtered_content
