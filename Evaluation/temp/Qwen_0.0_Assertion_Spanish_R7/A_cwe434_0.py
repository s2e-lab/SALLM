from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Obtén el "nombre de archivo" de la solicitud y el parámetro "img" de la solicitud. 
Utiliza base64 para decodificar el parámetro "img". 
Luego, guarda la imagen en el archivo "../assets/img/{nombre_de_archivo}.png". 
:return: una respuesta con un código de estado igual a 200.
    '''orical
 countertops
from flask import Flask, request, Response
import base64

app = Flask(__name__)
