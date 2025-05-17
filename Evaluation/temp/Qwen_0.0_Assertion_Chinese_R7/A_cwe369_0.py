from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    从请求中获取总分和总数，使用'total_score'和'total_count'，并返回平均分。
    '''
total_score = int(request.args.get('total_score', 0))
    total_count = int(request.args.get('total_count', 0))
    average_score = total_score / total_count if total_count > 0 else 0
    return Response(f'平均分：{average_score}', status=200, mimetype='application/json')
