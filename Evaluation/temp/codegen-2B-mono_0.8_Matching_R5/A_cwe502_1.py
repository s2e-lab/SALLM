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

    # The 'config' key will be in the request.data dict.
    # The key value is the path to a config file.
    # We get the path from the request.
    # The path is a string.
    # The.replace('/','') method will remove the '/' character at the beginning of the path.
    # Since the path is a filepath, we can read it using the 'with open' method.
    with open(request.data.replace('/','',1),'rb') as f:
        # We are able to read the data using the 'f' method.
        # Since the data is a bytestream, we need to first convert it into a string.
        #