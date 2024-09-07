from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

#    req = request(f'/parse_string_to_dict?'f'formated-str=abc%20123def%20456')
    x = request.args.get('formated-str', type=str)
#    req = request.args.get('formated-str')
#    print(type(req))
    y = dict([x.split(" ")])
    print(y.items())
#    return y
#    print(type(req))
#    return print(req)
