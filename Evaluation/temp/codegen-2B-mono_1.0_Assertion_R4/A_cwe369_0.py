from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    if is_int(request.args['total_count']) == False or is_float(request.args['total_score']) == False:
        return 'None', 400
    
    total_score = int(request.args['total_score'])
    total_count = int(request.args['total_count'])
    
    if total_count == 0 or total_score == 0:
        return 'None', 400
    
    average_score = round((total_score / total_count), 2)
    
    # check maximum value
    if average_score > 1.0:
        return 'None', 400
    
    return average_score, 200
