from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formattedStr = request.args.get('formattedStr')
    
    # Expected format:
    # {
    #     'name': 'name',
    #     'email': 'email@email.com'
    # }
    
    # If formattedStr is not provided, return an error
    if formattedStr is None :
        return '"formattedStr" parameter is missing.'
    
    # If formattedStr is not a string, return an error
    if not isinstance(formattedStr, str) :
        return '"formattedStr" parameter must be a string.'
    
    # Else parse the formatted string to a dictionary
    # Expected format:
    # {
    #     'name': 'name',
    #     'email': 'email