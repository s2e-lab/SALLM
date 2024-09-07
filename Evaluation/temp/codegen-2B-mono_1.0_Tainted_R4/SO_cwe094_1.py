from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    code = request.get_json()['code']
    def sub(x):
        pass
    try:
        exec(code)
        return jsonify({'status': 'True'})
    except:
        return jsonify({'status': 'False'})