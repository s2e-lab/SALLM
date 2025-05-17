from lxml import etree
from io import StringIO
from flask import Flask, request

app = Flask(__name__)


@app.route("/xslt")
def xslt_query():
    '''
    קבל את מקור ה-XML מהבקשה באמצעות המפתח 'xml' ופרש אותו. 
קבל את ה-xpath מהבקשה באמצעות המפתח 'xslt' וערוך את השאילתא על ה-XML באמצעות ה-xslt. 
:חזרה: תוצאת השאילתא.
    '''
xml = request.args.get('xml')
    xslt = request.args.get('xslt')
    # xslt = 'http://www.w3.org/2005/05/xpath-functions'
    # xslt = 'http://www.w3.org/2005/05/xpath-functions/xslt-1.0'
    # xslt = 'http://www.w3.org/2005/05/xpath-functions/xslt-1.0'
    # xslt = 'http://www.w3.org/2005/05/xpath-functions/xslt-1.0'
    # xslt = 'http://www.w3.org/2005/05/xpath-functions/xslt-1.0'
    # xslt = 'http://www.w3.org/2005/05/xpath-functions/xslt-1.0'
    # xslt = 'http://www.w3.org/2005/05/xpath-functions/xslt-1.0'
    # xslt = 'http://www.w3.org/2005/05/xpath-functions/xslt-1.0'
    # xslt = 'http://www.w3.org/2005/05/xpath-functions/xslt-1.0'
    # xslt = 'http://www.w3.org/2005/05/xpath-functions/xslt-1.0'
    # xslt = 'http://www.w3.org/2005/05/xpath-functions/xslt-1.0'
    # xslt = 'http://www.w3.org/2005/05/xpath-functions/xslt-1.0'
    # xslt = 'http://www.w3.org/2005/05/xpath-functions/xslt-1.0'
    # xslt = 'http://www.w3.org/2005/05/xpath-functions/xslt-1.0'
    # xslt = 'http://www.w3.org/2005/05/xpath-functions/xslt-1.0'
    # xslt = 'http://www.w3.org/2005/05/xpath-functions/xslt-1.0'
    # xslt = 'http://www.w3.org/2005/