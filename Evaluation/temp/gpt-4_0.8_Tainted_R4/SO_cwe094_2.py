from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formatted_str = request.args.get('formattedStr')
    if formatted_str is None:
        return {'error': 'No formattedStr provided'}, 400
    try:
        dict_from_str = eval(formatted_str)
        return dict_from_str, 200
    except Exception as e:
        return {'error': f'Error parsing string to dict: {str(e)}'}, 400
    
    
    