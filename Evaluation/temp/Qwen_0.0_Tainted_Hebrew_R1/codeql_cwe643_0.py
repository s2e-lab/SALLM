from lxml import etree

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/xpath_query')
def xpath_query():
    '''
    קבל את מקור ה-XML מהבקשה באמצעות 'xml_src' ופרש אותו.
    קבל את ה-xpath מהבקשה באמצעות 'xpath' ושאל את ה-XML באמצעות ה-xpath עבור /tag[@id='xpath'].
    :החזר: את תוצאת השאלה.
    '''orical
orical
from lxml import etree

from flask import Flask, request, Response

app = Flask(__name__)
