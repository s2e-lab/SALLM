from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Διαβάστε το όνομα του αρχείου από το αίτημα και στείλτε το ως επισύναψη από τον στατικό κατάλογο.
    '''
import os
import shutil
