from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''

    first_name = "No name!"

    # GET THE FIRST NAME FROM THE REQUEST
    if request.args:
        first_name = request.args.get("first_name")
    # GENERATE THE RESPONSE AND RETURN
    response = make_response(f"Greetings, {first_name}")
    return response
