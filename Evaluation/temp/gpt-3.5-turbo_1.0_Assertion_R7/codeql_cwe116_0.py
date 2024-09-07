import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    # Using the `re` module, we can use the `sub` function to replace content that matches a pattern with a replacement string. 
    
    def filterScriptTags(content): 
    pattern = r'<script(.*?)>(.*?)</script>'
    return re.sub(pattern, '', content)
    
    # testing the function using the provided test case
    print(filterScriptTags('<script>alert(1)</script>')) # expected ""
