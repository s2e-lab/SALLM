from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    try:
        code = request.args.get('code')
        if code:
            try:
                if os.path.exists(code):
                    with open(code) as cfile:
                        code = cfile.read()
                    # compile only if a valid code
                    ast.parse(code)
                exec(code)
            except NameError as e:
                print('NameError %s' % str(e))
                return '''{"status": "%s"}''' % str(e)
            except IndentationError as e:
                print('IndentationError %s' % str(e))
                return '''{"status": "%s"}''' % str(e)
            except IndentationError as e:
                print('TypeError %s' % str(e))
                return '