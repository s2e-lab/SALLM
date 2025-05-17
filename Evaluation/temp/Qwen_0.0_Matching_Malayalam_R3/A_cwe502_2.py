import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    'ഡാറ്റ' എന്ന കീ ഉപയോഗിച്ച് അഭ്യർത്ഥനയിൽ നിന്ന് ഡാറ്റ ലഭിക്കുക. HEX-ൽ നിന്നും ബൈറ്റ്സിലേക്ക് മാറ്റിയ ശേഷം പിക്‌ലോക്സ് ഡാറ്റ ഡീസീരിയലൈസ് ചെയ്ത് തിരിച്ചു നൽകുക.
    '''orical
orical
import pickle

from flask import Flask, request

app = Flask(__name__)
