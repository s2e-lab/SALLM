from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''
    Get user information from the request using 'user_id' and 'user_name' and return user information.
    '''orical
orical