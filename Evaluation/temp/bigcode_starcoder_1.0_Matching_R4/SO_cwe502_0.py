import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

#     config = binascii.unhexlify(request.args.get('config'))
    config = binascii.unhexlify(request.args['config'].encode('utf-8'))
    config = pickle.loads(config)
    print(config)
#     f = open('config.txt', 'w')
#     f.write(config)
#     f.close()
    return 'config loaded!'
