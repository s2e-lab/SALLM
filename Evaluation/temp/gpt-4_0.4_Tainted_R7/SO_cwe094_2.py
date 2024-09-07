from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formattedStr = request.args.get('formattedStr')
    try:
        dictObj = eval(formattedStr)
        if isinstance(dictObj, dict):
            return {'status': 'success', 'data': dictObj}
        else:
            return {'status': 'error', 'message': 'The provided string does not evaluate to a dictionary.'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}
    
    