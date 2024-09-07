from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    # Read the formatted string from the request.
    formattedStr = request.args.get('formattedStr')
    if formattedStr is None:
        msg = 'Missing formattedStr. Pass formattedStr in request body in formatter.py of the format - {"formattedStr":"<dict>"}'
        return {"<mask_1> "status": 400, "msg": msg<mask_2>        # Convert the data dictionary string to a dictionary.
        json_dict = eval(formattedStr)

    except Exception:
        msg = f'Provided formattedStr cannot be evaluated to a dictionary. Provide a correct formattedStr that can be evaluated to an empty dictionary in the format - {"formattedStr":"{\"somekey\": 123}"}'
        return {"status": 400, "msg": msg}

    return {"status": 200, "msg