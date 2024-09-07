import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    filterScripts = re.compile(r'<script[^<>]*>.*?</script>', re.MULTILINE)
    cleaned_html = filterScripts.sub("", content)
    return cleaned_html
