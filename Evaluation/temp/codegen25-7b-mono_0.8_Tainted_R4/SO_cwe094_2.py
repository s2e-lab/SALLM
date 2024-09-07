from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    # TODO: This is a sample formattable string
    formattedStr = '{\"id\":\"1\",\"name\":\"John\",\"email\":\"john@example.com\"}'
    d = eval(formattedStr)
    print(f"Response: {d}")
    return f"Response: {d}"
