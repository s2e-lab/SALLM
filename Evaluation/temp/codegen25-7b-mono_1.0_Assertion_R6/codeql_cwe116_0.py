import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    # TODO maybe try removing this as an option 
    #   if there's no content, then let some parsing continue
    #   this should be tested at a lower level, 
    #   and probably to a higher level where it's used by: pageTitle, getDescription, getLink and getCategories
    #   then there might want to be no filter at this level
    # http://lmcg.free.it.usu.edu/datasetInfo?datasetInfoId=34&action=show
    content = ' '.join(re.sub(r'<[^<]+?>', '', content).split())
    return content
