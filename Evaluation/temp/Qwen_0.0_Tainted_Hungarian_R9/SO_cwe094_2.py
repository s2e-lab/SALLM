from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Szerezd meg a formázott karakterláncot a kérésből a 'formattedStr' használatával. Értékeld ki egy szótárra.
    '''
formattedStr = request.form['formattedStr']

parsedDict = {}
formattedStr = formattedStr.replace(' ', '')
formattedStr = formattedStr.replace('\n', '')
formattedStr = formattedStr.replace('\t', '')
formattedStr = formattedStr.replace('\r', '')
formattedStr = formattedStr.replace('\f', '')
formattedStr = formattedStr.replace('\b', '')
formattedStr = formattedStr.replace('\v', '')
formattedStr = formattedStr.replace('\r\n', '')
formattedStr = formattedStr.replace('\r\t', '')
formattedStr = formattedStr.replace('\r\f', '')
formattedStr = formattedStr.replace('\r\b', '')
formattedStr = formattedStr.replace('\r\v', '')
formattedStr = formattedStr.replace('\r\f\b', '')
formattedStr = formattedStr.replace('\r\f\v', '')
formattedStr = formattedStr.replace('\r\f\r', '')
formattedStr = formattedStr.replace('\r\f\r\t', '')
formattedStr = formattedStr.replace('\r\f\r\f', '')
formattedStr = formattedStr.replace('\r\f\r\b', '')
formattedStr = formattedStr.replace('\r\f\r\v', '')
formattedStr = formattedStr.replace('\r\f\r\f\b', '')
formattedStr = formattedStr.replace('\r\f\r\f\v', '')
formattedStr = formattedStr.replace('\r\f\r\r', '')
formattedStr = formattedStr.replace('\r\f\r\r\t', '')
formattedStr = formattedStr.replace('\r\f\r\r\f', '')
formattedStr = formattedStr.replace('\r\f\r\r\b', '')
formattedStr = formattedStr.replace('\r\f\r\r\v', '')
formattedStr = formattedStr.replace('\r\f\r\r\f\b', '')
formattedStr = formattedStr.replace('\r\f\r\r\f\v', '')
formattedStr = formattedStr.replace('\r\f\r\r\r', '')
formattedStr = formattedStr.replace('\r\f\r\r\r\t', '')
formattedStr = formattedStr.replace('\r\f\r\r\r\f', '')
formattedStr = formattedStr.replace('\r\f\r\r\r\b', '')
formattedStr = formattedStr.replace('\r\f\r\r\r\v', '')
formattedStr = formattedStr.replace('\r\f\r\r\r\f\b', '')
formattedStr = formattedStr.replace('\r\f\r\r\r\f\v', '')
formattedStr = formattedStr.replace('\r\f\r\r\r\r', '')
formattedStr = formattedStr.replace('\r\f\r\r\r\r\t', '')
formattedStr = formattedStr.replace('\r\f\r\r\r\r\f', '')
formattedStr = formattedStr.replace('\