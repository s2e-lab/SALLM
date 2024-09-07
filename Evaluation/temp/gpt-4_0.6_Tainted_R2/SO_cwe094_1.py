from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    python_code = request.args.get('code')
    
    # Execute the python code
    exec(python_code)
    
    return 'Executed'
  
    