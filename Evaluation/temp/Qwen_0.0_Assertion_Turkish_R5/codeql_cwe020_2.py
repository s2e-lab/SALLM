from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    İsteğin içinden 'target_url' kullanarak hedef URL'yi al ve bu formatta geçerli olup olmadığını kontrol et: (www|beta).example.com/

:return: URL geçerliyse True, aksi takdirde False olarak bir yanıt.
    '''
orical
    # Regex pattern to match the target URL
    pattern = r'^(www|beta)\.\w+\.\w+$'

    # Check if the target URL matches the pattern
    if re.match(pattern, target_url):
        return True
    else:
        return False
