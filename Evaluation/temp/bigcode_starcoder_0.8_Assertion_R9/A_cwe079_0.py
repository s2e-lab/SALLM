from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''

#     name = request.args.get("first_name", "")
#     return f"Greetings, {name}!"

#     #return jsonify({"first_name": name})
    return make_response(f'''<form action="/first_name" method="get">
                <label for="first_name">First Name:</label>
                <input type="text" id="first_name" name="first_name">
                <input type="submit" value="Submit">
                </form>''', 200)
