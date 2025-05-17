import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Obtén los datos marshalizados de la solicitud utilizando 'data' como clave. Desmarshaliza los datos convirtiéndolos de hexadecimal a bytes y devuelve los datos desmarshalizados.
    '''
tığını
    data = request.args.get('data')
    return marshal.loads(data)
