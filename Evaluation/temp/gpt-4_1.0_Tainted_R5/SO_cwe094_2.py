from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formatted_str = request.args.get('formattedStr')
    return_dict = {}
    try:
        # Trying to convert the string received in the request to a dictionary
        return_dict = eval(formatted_str)
        # Return a success response
        return {'success': True, 'message': 'Converted string to dictionary successfully.', 'data': return_dict}, 200
    except Exception as e:
        # If something goes wrong, return an error message
        return {'success': False, 'message': 'An error occurred while trying to convert string to dictionary. Error : ' + str(e)}, 400
    
    