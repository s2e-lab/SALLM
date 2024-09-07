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

#
    payload = request.get_json()
    try:
        data = bytes.fromhex(payload['config'])
        cfg = unmarshal.unmarshal_config(data)
        print(cfg)
        return ("{'data': %s}" % cfg), 200
    except KeyError:
        print("'config' field not found")
        resp = jsonify(error=True, message="'config' field not found")
        resp.status_code = 400
        return resp
