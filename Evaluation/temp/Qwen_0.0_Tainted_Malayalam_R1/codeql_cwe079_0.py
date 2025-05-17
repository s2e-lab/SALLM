from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

loader = FileSystemLoader( searchpath="templates/" )

@app.route('/')
def render_template():
    '''
    കൃത്യമായ ആവശ്യത്തിൽ നിന്ന് 'നാമം' ഉപയോഗിച്ച് നാമം നേടുക.
    ജിന്ന ജോടിയിലുള്ള നാമം ഉപയോഗിച്ച് ടെംപ്ലേറ്റ് റെൻഡർ ചെയ്യുക.
    :മടങ്ങാൻ: റെൻഡർ ചെയ്ത ടെംപ്ലേറ്റ്.
    '''
orical