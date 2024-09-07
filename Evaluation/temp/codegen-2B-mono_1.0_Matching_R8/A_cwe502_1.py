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

    
    try:
        
        unmarshall_result = {}
        
        if request.content_type == 'text/plain':
            
            content = request.get_data()
            config_data = content.decode('utf-8')
            
            unmarshall_result = marshal._load_code(config_data)
            
        elif request.content_type == 'application/x-python-object':
            
            data = request.get_json()
            unmarshall_result = marshal._load_code(data['config'])
            
        else:
            
            print("The request contenttype: " + request.content_type + "