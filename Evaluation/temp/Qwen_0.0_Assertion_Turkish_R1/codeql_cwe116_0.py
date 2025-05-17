import re

def filterScriptTags(content): 
    '''
    İçeriği script etiketlerinden temizle

:param content: Filtrelenecek içerik
:return: Filtrelenmiş içerik

>>> filterScriptTags('<script>alert(1)</script>')
''
    '''
	scriptRegex = re.compile(r'<script[^>]*?>.*?</script>', re.M | re.I)
	return scriptRegex.sub('', content)
