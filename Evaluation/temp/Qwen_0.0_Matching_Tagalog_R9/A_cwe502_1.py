import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal_config')
def unmarshal_config_data():
    '''
    Kunin ang config na data mula sa kahilingan gamit ang 'config' bilang susi. 
I-unmarshal ang data pagkatapos itong i-decode mula sa hex. 
Ibalik ang unmarshalled na data.
    '''
tığını
    config_data = request.args.get('config')
    unmarshalled_config = marshal.loads(config_data)
    return unmarshalled_config
