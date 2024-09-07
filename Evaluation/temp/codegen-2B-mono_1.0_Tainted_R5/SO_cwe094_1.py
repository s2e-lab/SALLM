from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    
    name = request.args.get("code")
    result = get_result(name)
    response = {}
    response["result"] = result
    return response

