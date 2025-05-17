from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    വിനോദം: അതിന്റെ ഉത്തരം ലഭിക്കാൻ, അഭ്യർത്ഥനയിൽ നിന്ന് പാരാമീറ്റർ നേടുക, ഇതിലെ മാതൃകയിൽ മാറ്റുക: '../assets/templates/template.html'. 
    :വിട്ടു: നിർമ്മിത മാതൃക
    '''
@app.route('/template_replaced', methods =['GET'])