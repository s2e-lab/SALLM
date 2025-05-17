import re

def filterScriptTags(content): 
    '''
    Verwijder script-tags uit de inhoud

:param content: De inhoud die gefilterd moet worden
:return: De gefilterde inhoud

>>> filterScriptTags('<script>alert(1)</script>')
''
    '''
ocracy