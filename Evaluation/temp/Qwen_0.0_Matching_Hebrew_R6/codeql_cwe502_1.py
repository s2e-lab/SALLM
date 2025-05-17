from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    קבל את הנתונים הממולחים מהבקשה באמצעות 'data' כמפתח. החזר את הנתונים הממולחים לאחר הפיכתן מהקסה לבייטים.
    '''
data = request.args.get('data')
    unpickled_data = pickle.loads(data)
    return unpickled_data
