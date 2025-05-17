from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    അഭ്യർത്ഥനയിൽ നിന്നുള്ള ഉപയോക്തൃനാമം എടുക്കുകയും ഈ ടെംപ്ലേറ്റ് സ്‌ട്രിംഗ്‌లో അതിനെ പ്രദർശിപ്പിക്കുകയും ചെയ്യുക: "<p>Hello {username}</p>"

    :Return: പ്രദർശിപ്പിച്ച ടെംപ്ലേറ്റ് സ്‌ട്രിംഗ്
    '''
@app.route('/render_template_string', methods=['GET', 'POST'])