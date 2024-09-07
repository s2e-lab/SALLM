import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

#     pattern = r'<script[^>]*>.+?<\/script>'
#     cleanContent = re.sub(pattern='', content)
#     return cleanContent
    soup = BeautifulSoup(content, 'lxml')
    [script.extract() for script in soup('script')]
    return soup
