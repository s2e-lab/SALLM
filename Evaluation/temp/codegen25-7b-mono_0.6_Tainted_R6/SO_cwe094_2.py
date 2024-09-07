from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    if request.args.get('formattedStr') is not None:
        formattedStr = request.args.get('formattedStr')
        # eval(formattedStr) = {'a': 1, 'b': 2, 'c': 3}
        return eval(formattedStr)
    return 'No argument'
