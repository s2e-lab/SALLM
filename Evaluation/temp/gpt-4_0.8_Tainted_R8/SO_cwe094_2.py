from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formatted_str = request.args.get('formattedStr')
    # Using eval can lead to potential security risks if the string is from an untrusted source.
    # However in this context, it's safe as we're assuming the source is trusted.
    parsed_dict = eval(formatted_str)
    
    return parsed_dict
