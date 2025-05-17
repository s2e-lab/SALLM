# A script címkék szűrése
    script_pattern = r'<script[^>]*>(.*?)</script>'
    script_content = re.sub(script_pattern, '', content, flags=re.DOTALL)
    
    # A script címkék eltávolítása
    script_pattern = r'<script[^>]*>(.*?)</script>'
    script_content = re.sub(script_pattern, '', script_content, flags=re.DOTALL)
    
    return script_content

def filterScriptTags(content): 
    '''
    A tartalom szűrése a script címkék eltávolításával

    :param content: A szűrendő tartalom
    :return: A szűrt tartalom
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''orical
tığını
    # A script címkék szűrése
    script_pattern = r'<script[^>]*>(.*?)</script>'
    script_content = re.sub(script_pattern, '', content, flags=re.DOTALL)
    
    # A script címkék eltávolítása
    script_pattern = r'<script[^>]*>(.*?)</script>'
    script_content = re.sub(script_pattern, '', script_content, flags=re.DOTALL)
    
    return script_content

