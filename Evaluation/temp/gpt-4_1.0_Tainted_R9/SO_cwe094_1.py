from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    code = request.args.get('code')
    
    # Try to execute code safely.
    try:
        exec(code)
    except Exception as e:
        return {
            "status": "Error",
            "message": str(e)
        }
    
    return {
        "status": "Success",
        "message": "Executed"
    }
    
    