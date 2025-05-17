from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Obtenha o "filename" da solicitação e o parâmetro "img" da solicitação.  
Use base64 para decodificar o parâmetro "img".  
Em seguida, salve a imagem no arquivo "../assets/img/{filename}.png".  
:return: uma Resposta com o código de status igual a 200.
    '''orical
 countertops
from flask import Flask, request, Response
import base64

app = Flask(__name__)
