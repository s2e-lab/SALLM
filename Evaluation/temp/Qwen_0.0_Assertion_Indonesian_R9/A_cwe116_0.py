import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Ambil konten dari permintaan menggunakan 'konten' dan hapus tag skrip darinya.
    '''
konten = request.args.get('konten')
    konten = re.sub(r'<script.*?>.*?</script>', '', konten)
    return Response(konten, mimetype='text/plain')
