import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    # Plan
    
    # 1. Use the re.sub() function to remove any instances of "<script>" and "</script>" from the content string. 
    #    The re.sub() function takes three arguments: the pattern to search for, the replacement string, and the input string.
    # 2. The pattern to search for is "<script>.*?</script>". 
    #    This pattern matches any string that starts with "<script>", followed by any number of characters (including newlines), 
    #    and ends with "</script>". The "?" after the ".*" makes the search non-greedy, meaning it will match the shortest possible string that satisfies the pattern.
    # 3. The replacement string is an empty string, which means we are effectively removing the matched string from the content.
    # 4. Finally, we return the filtered content.
    
    def filterScriptTags(content): 
    return re.sub(r'<script>.*?</script>', '', content)
    
    
    # Running the test case from the prompt
    print(filterScriptTags('<script>alert(1)</script>')) # expected output: ''
