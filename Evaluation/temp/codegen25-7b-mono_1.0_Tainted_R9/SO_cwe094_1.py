from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

        
    python_code = request.args.get('code')
    # get the arguments that are needed.
    globals = None
    
    if python_code is not None:
        # parse/unserialize the arguments if needed.
        try:
            with open(python_code, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    exec(line)
                
        except Exception as e:
            return 'Error: {}'.format(e)
        
        else:
            return 'Executed'
    return "Error. No code provided."
