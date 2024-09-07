from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    # Get the formatted string from the request.
    formattedStr = request.args.get('formattedStr')
    # Eval it to a dictionary.
    dict = eval(formattedStr)
    # Return the dictionary.
    return dict
