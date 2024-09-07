from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    try:
        return eval(request.files['file_contents'].read().decode("utf-8"))
    except:
        return jsonify({"message" : "Unable to evaluate: please contact the admins"})
