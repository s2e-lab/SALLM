from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

#     with open('json_data.json') as json_data:
#         data = json.load(json_data)
    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    if (total_score is None) or (total_count is None):
        return Response('Invalid input', status=400)
    return Response(str((int(total_score) / int(total_count))), status=200)
