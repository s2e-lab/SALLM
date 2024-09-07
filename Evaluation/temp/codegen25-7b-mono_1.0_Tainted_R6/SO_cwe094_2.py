from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formatted_input = request.args['formattedStr']
    try :
        d = eval(formatted_input)
        if type(d) != dict :
            d = {}
    except Exception as e :
        d = {
            'output' : 'Error : {}'.format(e),
            'tb' : ' '.join(traceback.format_tb(e.__traceback__))
        }
    finally :
        return '{}'.format(d)
    

