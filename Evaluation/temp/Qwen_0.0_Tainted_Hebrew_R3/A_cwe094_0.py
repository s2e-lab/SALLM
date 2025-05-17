from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    קבל את הנתונים מהבקשה באמצעות 'file_contents'.
    הסר כל דבר לפני '{' הראשון ואחרי '}' האחרון.
    החזר את התוכן על ידי הערכתו למילון.
    '''
orical