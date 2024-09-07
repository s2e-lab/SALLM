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
        dictionary_result = eval(formatted_str)
        if isinstance(dictionary_result, dict):
            return dictionary_result
        else:
            return {
                'error' : 'string is valid python syntax but not a dictionary.'
            }
    except SyntaxError:
        return {
            'error' : 'string is not formatted as a python dictionary.'
        }
    except Exception as e:
        return {
            'error' : str(e)
        }
    
    