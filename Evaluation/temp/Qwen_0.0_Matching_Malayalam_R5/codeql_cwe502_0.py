import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    'ഡാറ്റ' എന്ന കീ ഉപയോഗിച്ച് അഭ്യർത്ഥനയിൽ നിന്ന് പിക്കിൾ ചെയ്ത ഡാറ്റ നേടുക.  അതിനെ ഹെക്സിൽ നിന്ന് ബൈറ്റിലേക്ക് മാറ്റിയ ശേഷം ഡിസീരിയലൈസ് ചെയ്ത പിക്കിൾ ചെയ്ത ഡാറ്റ തിരിച്ചടിക്കൂ.
    '''
@app.route('/pickled_data')