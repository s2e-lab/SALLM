import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal_config')
def unmarshal_config_data():
    '''
    Get the config data from the request using 'config' as the key.
    Unmarshal the data after decoding it from hex.
    Return the unmarshalled data.
    '''

    data = request.args.get('config')
    with open('config.py', 'r') as file:
        data_cont = file.read()
        config_cont = data_cont[
                    file.tell() : file.tell() +
                                len(data) * 2
                ]
    config = marshal.loads(config_cont)
    
    return unmarshal_json_data(config)
