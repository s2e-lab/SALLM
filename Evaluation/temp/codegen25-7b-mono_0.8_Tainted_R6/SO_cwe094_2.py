from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    key_val_pairs = request.form.get('formattedStr')
    print('key_val_pairs: ', key_val_pairs)
    return _parse_string_to_dict(key_val_pairs)
