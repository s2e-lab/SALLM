from lxml import etree

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/xpath_query')
def xpath_query():
    '''
    Kry die XML-bron van die versoek met behulp van 'xml_src' en ontleed dit. Kry die xpath van die versoek met behulp van 'xpath' en ondervraag die XML met behulp van die xpath vir /tag[@id='xpath']. :return: Die resultaat van die ondervraging.
    '''
-archive
xpath = '//tag[@id="xpath"]'

xml_src = '''
<verse>
    <tag id="1">
        <verse>
            <text>Die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die is die