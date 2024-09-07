from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    try:
        formatted_str = request.args.get('formattedStr')
        dictionary = eval(formatted_str)
        return dictionary
    except Exception as e:
        return {'error': str(e)}
    
    