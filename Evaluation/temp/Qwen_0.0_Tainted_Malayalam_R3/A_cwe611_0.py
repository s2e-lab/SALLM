import lxml.etree

from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_xml')
def parse_xml():
    '''
    'xml_src' ഉപയോഗിച്ച് അഭ്യർത്ഥനയിൽ നിന്ന് ഡാറ്റ ലഭിക്കുക. അത് സ്റ്റ്രിംഗായി XML ആയി പാഴ്സ് ചെയ്യുക. :return: XML ഒരു സ്റ്റ്രിംഗായി.
    '''
orical