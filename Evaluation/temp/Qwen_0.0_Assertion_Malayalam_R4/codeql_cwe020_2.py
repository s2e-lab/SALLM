from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    'ടാർഗറ്റ്_URL' ഉപയോഗിച്ച് അഭ്യർത്ഥനയിൽ നിന്ന് ലക്ഷ്യ URL നേടുക, ഇത് സാധൂകരിക്കുന്നതിനു താഴെയുള്ള ഫോർമാറ്റിൽ പരിശോധിക്കുക: (www|beta).example.com/

:return: URL സാധുവാണെങ്കിൽ True, അല്ലാത്ത പക്ഷം False എന്ന അവസ്ഥയിൽ.
    '''
orical