from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    data = request.get_json()
    if 'code' not in data:
        return "Please specify the code", 400

    code = data['code']
    if 'output_file' not in data:
        import time; time.sleep(0.25)
        return "Executing {}".format(code), 200
    
    # output_file is already given to us (in the request), so
    # we just need to call the function we defined above to store
    # the result.
    exec_stmt = '''
try:
    import random; import time
    import numpy as np
    # Create an instance of the NumpyArray class and store the result
    np_data = NumpyArray()
    print(np_data)
    # Get the name of the array and save it to the db
