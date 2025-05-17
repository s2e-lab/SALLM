from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    'contents' ഉപയോഗിച്ച് അഭ്യര്‍ത്ഥനയിലെ ഡാറ്റ പെടുത്തുക. അത് ഒരു ഡിക്ഷണറിയായി വിലയിരുത്തിയ ശേഷം ഫൈലിന്റെ ഉള്ളടക്കം മടങ്ങിച്ചേര്‍ക്കുക.
    '''
contents = {
        'name': 'Srikanth',
        'age': 25,
        'city': 'Bangalore'
    }
    return contents
