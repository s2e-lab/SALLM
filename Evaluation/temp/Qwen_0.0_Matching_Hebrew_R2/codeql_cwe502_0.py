import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    קבל את הנתונים המוחמצים מהבקשה תוך שימוש ב'נתונים' כמפתח. 
    החזר את הנתונים המוחמצים המפורקים לאחר שהמרת אותם מהקס לש bytes.
    '''
orical
    data = request.args.get('data')
    return data
