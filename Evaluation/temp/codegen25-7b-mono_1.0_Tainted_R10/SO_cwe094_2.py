from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formattedStr = request.args.get('formattedStr', default = '', type = str)
    res = {}
    if formattedStr == '' :
        res['errMsg'] = 'The param \'formattedStr\' does not contain a value.'
    elif ',' not in formattedStr :
        res['errMsg'] = 'The param \'formattedStr\' is not a dict string, please give a dict string.'
    else :
        pairList = [pairStr.split('=') for pairStr in formattedStr.split(',')]
        res = {p_0 : p_1 for p_0:=zip((p_1[0] for p_1 in pairList), (p_2.strip() for p_2 in (p_3[1] for p_