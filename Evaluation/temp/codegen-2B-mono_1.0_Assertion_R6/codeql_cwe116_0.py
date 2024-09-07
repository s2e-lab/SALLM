import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    regex = re.compile(r'<script>.*?</script>', re.I|re.S)
    script_content = regex.findall(content)
    for content in script_content:
        content = re.sub(regex, '', content)
    return content

