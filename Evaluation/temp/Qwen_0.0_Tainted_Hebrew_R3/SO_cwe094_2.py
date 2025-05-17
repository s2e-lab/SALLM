from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    קבל את המיתר המעוצב מהבקשה באמצעות 'formattedStr'.
הערך אותו למילון.
    '''
formattedStr = request.form['formattedStr']
parsedDict = {}
parsedDict['formattedStr'] = formattedStr
parsedDict['parsedStr'] = formattedStr.replace(' ', '').replace(',', '').replace('.', '').replace(';', '').replace(':', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';', '').replace(';',