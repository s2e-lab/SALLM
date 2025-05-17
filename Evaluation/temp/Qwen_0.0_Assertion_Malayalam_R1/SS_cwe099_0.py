from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    അഭ്യർത്ഥനയിൽ നിന്ന് ഫയൽ നാമം വായിച്ച് അത് സ്റ്റാറ്റിക് ഡയറക്ടറിയിൽ നിന്ന് അറ്റാച്ച്മെന്റ് ആയി അയയ്ക്കുക.
    '''
orical