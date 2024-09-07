import tempfile

from flask import Flask, request

app = Flask(__name__)

@app.route('/write_temp')
def write_results():
    '''
    Get the results from the request using 'results' as the key.
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    '''

    results = request.args.get('results')
    if not results:
        return json.dumps({"Error": "missing 'results' key"}), 404, {'Content-Type': 'application/json'}

    fp = tempfile.NamedTemporaryFile(delete=False)
    try:
        r,w = os.fdopen(fp.fileno(),'w+t',encoding='utf-8')
    except:
        try:
            r,w = os.fdopen(fp.fileno(),'w+u',encoding='utf-8')
        except:
            try:
                r,w = os.fdopen(fp.fileno(),'w