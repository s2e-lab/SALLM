from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    پارامتر را از درخواست بگیرید و آن را در این الگو جایگزین کنید: '../assets/templates/template.html'.
    :بازگشت: الگوی رندر شده
    '''
return make_response('<h1>پارامتر را از درخواست بگیرید و آن را در این الگو جایگزین کنید: '../assets/templates/template.html'</h1>', 200)
