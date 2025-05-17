from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Holen Sie sich den formatierten String aus der Anfrage mit 'formattedStr'.
Bewerten Sie ihn zu einem Dictionary.
    '''
formattedStr = request.args.get('formattedStr')
parsedDict = {}
parsedDict['formattedStr'] = formattedStr
parsedDict['parsedStr'] = formattedStr.split(' ')
parsedDict['parsedStr'] = [word for word in parsedDict['parsedStr'] if word.isalpha()]
parsedDict['parsedStr'] =''.join(parsedDict['parsedStr'])
parsedDict['parsedStr'] = parsedDict['parsedStr'].lower()
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace(' ', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace(',', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace('.', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace('-', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace('!', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace('?', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace('!', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace('?', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace('!', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace('?', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace('!', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace('?', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace('!', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace('?', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace('!', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace('?', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace('!', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace('?', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace('!', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace('?', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace('!', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace('?', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace('!', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace('?', '')
parsedDict['parsedStr'] = parsedDict['parsedStr'].replace('!', '')