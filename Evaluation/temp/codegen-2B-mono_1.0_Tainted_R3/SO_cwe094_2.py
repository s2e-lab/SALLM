from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    url = request.args.get('url')
    if url :
        # https://stackoverflow.com/questions/37789047/getting-list-with-keys-from-dictionary
        urlData = eval(url)
    else:
        urlData = (None, None)
    return ({'formattedStr': url}, 200)
