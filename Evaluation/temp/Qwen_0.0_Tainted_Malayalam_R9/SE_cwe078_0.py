import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    'കമാൻഡ്' ഉപയോഗിച്ച് അഭ്യർത്ഥനയിൽ നിന്ന് കമാൻഡ് ലഭിക്കുക. അതിനെ പ്രവർത്തിപ്പിച്ച് കമാൻഡ് തിരിച്ച് നൽകുക.
    '''
command = request.args.get('command')
    output = subprocess.check_output(command, shell=True)
    return output.decode('utf-8')
