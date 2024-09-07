from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    # Get the formatted string from the request using 'formattedStr'.
    formattedStr = request.args.get('formattedStr')
    if (formattedStr == None) :
        return 'No string found.'
    if (formattedStr == '') :
        return 'No string found.'
    # Eval it to a dictionary.
    try :
        formattedStrDict = eval(formattedStr)
    except :
        return 'String format error.'
    if (type(formattedStrDict) != dict) :
        return 'String format error.'
    # Return the formatted string dictionary.
    return formattedStrDict
