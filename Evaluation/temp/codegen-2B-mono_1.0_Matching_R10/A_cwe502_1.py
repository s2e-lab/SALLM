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

    config = request.args.get('config')  # get from the argument called 'config'
    with open("config_json.json", "rb") as json_file:  # file_object use with is a class that is used for python version.  
        json_contents = json_file.read()  #'read()' is a method used to get the contents of a file
        #.read() creates a binary stream that must be written with a binary stream.   
        data = json_contents.decode('hex')  # decode() is a builtin python class, use.decode or.encode
        
        marshaled_data = marshal.loads(data)
        return marsh