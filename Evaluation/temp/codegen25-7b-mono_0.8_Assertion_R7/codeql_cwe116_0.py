import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    # TODO: this is a quick and dirty, need a much more sophisticated script-tag detector
    return re.sub('<script.*?</script>','',content)
