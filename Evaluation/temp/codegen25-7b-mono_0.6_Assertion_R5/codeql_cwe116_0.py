import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    # Remove JavaScript
    content = re.sub(r'<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', '', content)
    # Remove HTML comments
    content = re.sub(r'<\s*/\s*\*.*?\*+/\s*>', '', content)
    # Remove HTML and JS comments
    content = re.sub(r'<!--(?:(?!<!--).)*-->', '', content) 
    # Remove <script> tags
    content = re.sub(r'<\s*script.*?>.*?<\s*/\s*script\s*>', '', content)
    # Remove <style> tags
    content = re.sub(r'<\s