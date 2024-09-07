import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    # Create a regular expression pattern to match script tags
    pattern = re.compile(r'<script.*?>.*?</script>', re.DOTALL)
    
    # Use the sub() function to replace the matched script tags with an empty string
    filtered_content = re.sub(pattern, '', content)
    
    return filtered_content
