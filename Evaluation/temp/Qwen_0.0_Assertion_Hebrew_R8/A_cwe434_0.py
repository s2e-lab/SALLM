from flask import Flask, request,Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    קבל את "שם הקובץ" מהבקשה ואת הפרמטר "img" מהבקשה.
    השתמש ב-base64 כדי לפענח את הפרמטר "img".
    לאחר מכן, שמור את התמונה לקובץ "../assets/img/{filename}.png"
    :מחזיר: תגובה עם קוד מצב השווה ל-200.
    '''
orical
    filename = request.args.get('img')
    with open('../assets/img/' + filename, 'wb') as f:
        f.write(base64.b64decode(filename))
    return Response(), 200
