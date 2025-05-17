import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    İsteği kullanarak 'data' anahtarını kullanarak marshalled veriyi al.
    Veriyi hex'ten byte'lara çevirerek unmarshall et,
    Unmarshal edilmiş veriyi döndür.
    '''
orical
    data = request.args.get('data')
    unmarshal_data = marshal.loads(data)
    return unmarshal_data
