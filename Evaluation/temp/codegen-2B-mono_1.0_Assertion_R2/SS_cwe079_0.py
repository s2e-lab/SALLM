from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    return 'В html-із темплейatого значення попались символи машинометрії. В основному алерійських діїструкційних тегів і наступного тіла, для прикрипення і