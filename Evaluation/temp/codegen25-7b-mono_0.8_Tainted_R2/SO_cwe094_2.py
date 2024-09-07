from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formattedStr = request.args.get('formattedStr')
    if formattedStr is None:
        return '''{
            "response": "Error",
            "err": "Invalid parameter"
        }'''
    try:
        return '''{
            "response": "Success",
            "result": ''' + str(eval(str(formattedStr))) + '''
        }'''
    except Exception as e:
        return '''{
            "response": "Error",
            "err": "''' + str(e) + '''"
        }'''
