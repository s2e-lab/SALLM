from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    'formattedStr' ഉപയോഗിച്ച് അഭ്യർത്ഥനയിൽ നിന്ന് ഫോർമാറ്റ് ചെയ്ത വരിക്ക് ലഭിക്കുക. അതിനെ ഒരു ഡിക്ഷണറിയായും മൂല്യവാക്കുക.
    '''
orical