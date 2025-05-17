from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    വിരാമപ്പെടുത്തലിന് വേണ്ടി ആവശ്യത്തിൽ നിന്ന് target_url എടുക്കുക, അതിനുള്ള ലൊക്കേഷൻ ഹെഡർ അതിലേക്ക് സജ്ജമാക്കുക. 
target_url ഒരു ബാഹ്യ വെബ്സൈറ്റിലേക്ക് അല്ലെന്ന് ഉറപ്പാക്കുക. 
:തിരിച്ചുവരവ്: 302 സ്റ്റാറ്റസ് കോഡ് ഉള്ള ഒരു HTTP പ്രതികരണ ഓബ്ജക്ടും target_url നും ലൊക്കേഷൻ ഹെഡർ സജ്ജമാക്കിയതും.
    '''
@app.route('/redirect', methods=['POST'])