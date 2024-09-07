import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    start_script = re.compile('<script')
    end_script = re.compile('</script>')
    start_comment_script = re.compile('<!--')
    end_comment_script = re.compile('-->')
    comment_script = re.compile('<!--')
    
    return start_script.sub('', content), end_script.sub('', content), start_comment_script.sub('', content), end_comment_script.sub('', content),comment_script.sub('', content)
