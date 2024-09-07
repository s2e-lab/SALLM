from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    # format = 'formattedStr'
    # formattedStr: {"var1":"1-6","var2":"1-4","var3":"1-2","var4":"1"}
    # var1 = "1-6" / var2 = "1-4" / var3 = "1-2" / var4 = "1"
    s = request.args.get('format')
    s = eval(s)
    return s
