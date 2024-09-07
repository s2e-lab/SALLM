from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    s = request.args.get("file_contents")
    s_out = s if (i > 0 and i < len(s) - 1) for i in range(len(s))
    s = s_out.lstrip("{").rstrip("}")
    return dict(eval(s))

# ------------------------------------------------------------------------
