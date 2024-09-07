from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    str_to_dict = request.args.get('formattedStr')
    dict_ = eval(str_to_dict)
    return dict_ 
    
    