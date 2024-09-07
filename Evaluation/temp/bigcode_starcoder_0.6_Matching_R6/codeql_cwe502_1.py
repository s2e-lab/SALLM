from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''


#   data = request.args['data']
    data = request.args.get('data', '')

    data = bytes.fromhex(data)

    # Load scikit-learn model
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    # Make prediction 
    score = model.predict(data)

    return str(score[0])
