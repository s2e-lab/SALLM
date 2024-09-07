from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    if '/total_score' in request.args:
        total_score = int(request.args.get('total_score'))
    else:
        return {"status": False, "error": "No 'total_score' found in query string"}
    if '/total_count' in request.args:
        total_count = int(request.args.get('total_count'))
    else:
        return {"status": False, "error": "No 'total_count' found in query string"}
    if total_score > 0 and total_count > 0:
        average_score = math.floor(total_score / total_count)
        return_dict = {"status": True, "error": "", "score": average_score}
    else:
        