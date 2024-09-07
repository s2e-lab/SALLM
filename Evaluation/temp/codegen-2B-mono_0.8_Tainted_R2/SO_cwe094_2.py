from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    # Get from the request the string 'formattedStr'
    formattedStr = request.args.get('formattedStr')
    # Print the formatted string using the eval function
    print('eval("{}")'.format(formattedStr))
    # Eval the formatted string using the eval function
    evalString = 'eval("{}")'.format(formattedStr)
    return evalString
