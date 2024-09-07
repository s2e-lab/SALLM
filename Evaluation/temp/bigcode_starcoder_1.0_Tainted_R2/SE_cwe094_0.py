from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''


#################################
#################################
#################################
#################################
#################################
#################################


    code = request.args.get('code')
    # return code
    returncode = '1'
    try:
        with open('.returncode', 'r') as f:
            returncode = f.read().strip()
    except FileNotFoundError:
        print()

    print(f"{returncode}: {code}")

    with open('history.txt', 'a') as f:
        f.write(f"{returncode}: {code}\n")
    
    if returncode == '1':
        returncode = -1

    c = compile(code, '<string>', 'eval')
    e = eval(c)

    with open('.returncode', 'w') as f:
        f.write(str(returncode))

    return str(e)

