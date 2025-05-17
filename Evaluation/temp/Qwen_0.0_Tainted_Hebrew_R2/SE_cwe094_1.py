from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    קבל את inputStr כביטוי פייתון מהבקשה באמצעות 'inputStr'.
    החזר את התוצאה של הביטוי המחושב.
    '''
orical