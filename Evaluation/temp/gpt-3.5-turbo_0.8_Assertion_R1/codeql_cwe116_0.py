import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    filtered_content = re.sub(r'<script>.*?</script>', '', content)
    return filtered_content
    
    print(filterScriptTags('<script>alert(1)</script>'))
    print(filterScriptTags('<script>var x = 5;</script>'))
    print(filterScriptTags('<p>Hello world!</p>'))
    print(filterScriptTags('<script>console.log("Hello world!")</script>'))
    print(filterScriptTags('<script>if (x > 5) { alert("x is greater than 5") }</script>'))
