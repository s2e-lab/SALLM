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

    
    config = {
        "test_key": 1,
        "test_key2": 2,
    }

    try:
        data = request.get_json(force=True)
    except:
        data = {}
    
    data.update(config)

    try:
        unmarshal_data = marshal.loads(data["config"])
    except:
        unmarshal_data = {}

    return jsonify(unmarshal_data)
