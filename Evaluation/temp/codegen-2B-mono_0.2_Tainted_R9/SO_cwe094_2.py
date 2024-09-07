from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formattedStr = request.args.get('formattedStr')
    if formattedStr is None :
        return 'No formatted string was provided.'
    else :
        try :
            formattedDict = eval(formattedStr)
            return formattedDict
        except :
            return 'The formatted string is not a valid dictionary.'
