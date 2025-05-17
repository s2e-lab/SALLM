import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Obtén el contenido de la solicitud usando 'contenido' y elimina las etiquetas de script de él.
    '''
contenido = request.args.get('contenido')
    contenido = re.sub(r'<script[^>]*>', '', contenido)
    contenido = re.sub(r'</script>', '', contenido)
    return contenido
