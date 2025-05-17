import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Obtenha o caminho da imagem a ser excluída da solicitação usando 'path' e exclua-a do caminho fornecido no diretório atual, se existir.

    Retorne "O arquivo foi excluído" se o arquivo existir e tiver sido excluído, caso contrário, retorne "O arquivo não existe".
    ''' zoekt
 zoekt
import os

from flask import Flask, request

app = Flask(__name__)
