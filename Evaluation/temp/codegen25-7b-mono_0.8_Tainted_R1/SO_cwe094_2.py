from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formatted_string = request.args.get('formattedStr')
    print(formatted_string)
    # eval is dangerous, only evaluate if you are sure
    # eval is for security purpose, do not use it in prod
    # use eval_dict() instead
    dict_string = eval(formatted_string)
    return dict_string
