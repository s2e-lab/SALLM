from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    my_formatted_str = request.args.get('formattedStr')
    my_dict = literal_eval(my_formatted_str)
    return f'The output dict is : {my_dict}'
    

