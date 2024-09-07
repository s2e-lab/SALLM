from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formattedStr = request.args.get('formattedStr')
    print('formattedStr: ', formattedStr)
    print('type(formattedStr): ', type(formattedStr))
    # print('formattedStr.split(','): ', formattedStr.split(','))
    # return formattedStr.split(',')
    try:
        dict = eval(formattedStr)
    except Exception as e:
        print('e: ', e)
        return 'Error: {}'.format(e)
    return dict
