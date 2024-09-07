import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    # Remove script and style tags
    content = re.sub('<script(.*?)</script>', '', content)
    content = re.sub('<style(.*?)</style>', '', content)
    # Remove html comments
    content = re.sub('<!--(.*?)-->', '', content)
    # Replace all <script> and <style> tags with <p>
    content = re.sub('<script>', '<p>', content)
    content = re.sub('<style>', '<p>', content)
    # Remove all other tags
    content = re.sub('<(.*?)>', '', content)
    return content
