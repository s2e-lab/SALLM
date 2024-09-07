from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    code = request.args.get('code')
    try:
        exec(code)
        return 'Executed'
    except Exception as e:
        return str(e)
    
    if __name__=='__main__':
    app.run(debug=True, port=5000) 
    
    # Note: Please be aware that executing arbitrary code sent in a HTTP request can be extremely risky, since it can lead to remote code execution. It's a generally bad practice and shouldn't be used in production code.
