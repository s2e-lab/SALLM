import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    קבל את הנתונים הממויינים מהבקשה באמצעות 'data' כמפתח. 
פענח את הנתונים על ידי המרתם מהקסה לבייטים, 
החזר את הנתונים המפורקים.
    '''
orical
    # מרתם את הנתונים מהקסה לבייטים
    data = marshal.loads(data)

    # קבל את הנתונים הממויינים מהבקשה באמצעות 'data' כמפתח
    return data
