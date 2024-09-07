from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total = int(request.args.get('total_score'))
    count = int(request.args.get('total_count'))
    result = {
       <mask_1> response = Response(response=result, status=200, mimetype='application/json')
    return response

