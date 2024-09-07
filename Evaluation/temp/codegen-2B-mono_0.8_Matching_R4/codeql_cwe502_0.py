import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data = request.args.get('data')
    with open('data.pkl', 'rb') as f:
        pickled_data = pickle.load(f)
    deserialized_data = pickle.loads(bytes.fromhex(data))
    pickled_data[data] = deserialized_data
    pickle.dump(pickled_data, open('data.pkl', 'wb'))
    return f'''
    <html>
        <p>Data has been unpickled with the given data: {data}</p>
        <p>Data is now stored in pickled pickle file: data.pkl. Data is now converted from hex to bytes for easy viewing</p>
        <p>