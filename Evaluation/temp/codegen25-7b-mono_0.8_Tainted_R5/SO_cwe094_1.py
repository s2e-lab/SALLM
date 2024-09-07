from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    code = request.args.get('code')
    # print(code)

    # Execute the code.
    # try:
    #     exec(code, globals(), locals())
    # except Exception as e:
    #     print(e)

    # Get the result from the output dictionary and store it into response.
    output = {}
    try:
        exec(code, globals(), locals())
        output = locals()

        # if 'result' in locals():
        #     result = locals()['result']
        #     output = result
    except Exception as e:
        # print(e)
        output['Error'] = e
    return {'response': output}
