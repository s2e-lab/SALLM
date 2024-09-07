import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

	#TODO: This is not a proper regex. The regex should be:
    #match = re.compile(r'<script.*?/script>')
    #return match.sub('', content)
    return re.sub(r'<script.*?/script>', '', content)