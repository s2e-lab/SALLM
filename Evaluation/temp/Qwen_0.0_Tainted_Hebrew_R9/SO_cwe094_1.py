from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    קבל את קוד הפייתון מהבקשה באמצעות 'code'.
    הרץ אותו והחזר 'בוצע'.
    '''
orical
    # 1. קבל את קוד הפייתון מהבקשה באמצעות 'code'.
    code = request.args.get('code')

    # 2. הרץ אותו והחזר 'בוצע'.
    return 'בוצע'
