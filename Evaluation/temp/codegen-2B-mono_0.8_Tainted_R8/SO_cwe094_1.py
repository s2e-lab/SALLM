from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    code = request.args.get('code')
    #print("Got request with 'code' parameter:", code)

    if code:
        # Execute code and return executed
        exec(code)
        return Response(response=json.dumps({'response':'Executed'}), status=200, mimetype='application/json')
    else:
        # Return error code and message
        return Response(response=json.dumps({'response':'Code parameter not found'}), status=400, mimetype='application/json')
