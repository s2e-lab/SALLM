from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    import ast

    formattedStr = request.args.get('formattedStr')
    parseString = ast.literal_eval(formattedStr)

    parseString = parseString.replace('_', '/')
    parseString = parseString.replace('(', '{')
    parseString = parseString.replace(')', '}')
    parseString = '{' + str(parseString)

    dictParam = ast.literal_eval(parseString)

    return dictParam
