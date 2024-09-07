from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    try:
        formattedStr = request.args.get('formattedStr')
        return eval(formattedStr)
    except Exception as e:
        print(str(e))
        return {'error': str(e)}

