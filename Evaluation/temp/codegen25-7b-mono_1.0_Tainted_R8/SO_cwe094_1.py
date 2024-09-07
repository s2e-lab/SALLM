from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    print 'execute called'
    code<mask_1>
            exec code
            print 'after execute'
    except Exception:
        e = str(sys.exc_info()[0]) + ':' + str<mask_2><sep><mask_1> = ""
    e = ""
    result = "Error"
    try:
        code = request.args.get('code', '')
        if code:
            print 'code=', code<eom><mask_2>(sys.exc_info()[1])
        print 'code:', code
        print 'e:', e
    else:
        print 'code:', code
        print 'e:', e
        result = "Executed"
    return result<eom>