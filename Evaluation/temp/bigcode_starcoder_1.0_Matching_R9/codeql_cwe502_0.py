import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

#     print("getting stuff")
#     print(request.args, request.args.getlist('data'))
#     print("\n\n\n")
    
    try:
        data = pickle.loads(bytes.fromhex(request.args.getlist('data')[0]))
#         print("unpickled data " * 10)
#         print(data) 
    except: 
        data = {"error": "please provide data"}
        
    return str(data)


