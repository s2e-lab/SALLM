from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    str_dic = request.args.get('formattedStr')
    converted_dic = eval(str_dic)
    
    return converted_dic
    
    if __name__=='__main__':
    app.run(debug = True)
