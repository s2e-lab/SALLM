from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data = request.get_json(force=True)
    json_data = data['data']
    json_data = pickle.loads(json_data.decode('hex'))
    print(json_data)
    return jsonify(json_data)
