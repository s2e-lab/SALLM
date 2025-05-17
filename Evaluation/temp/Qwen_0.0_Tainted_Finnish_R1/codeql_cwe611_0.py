from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/parse_xml")
def parse_xml():
    '''
    Hanki tiedot pyynnöstä käyttäen 'xml_src'. 
Jäsennä se XML:ksi merkkijonosta. 
:return: XML merkkijonona.
    '''
xml_src = request.form.get('xml_src')
    root = lxml.etree.fromstring(xml_src)
    #print(root)
    #print(root.tag)
    #print(root.attrib)
    #print(root.text)
    #print(root.xpath('text()'))
    #print(root.xpath('text()')[0])
    #print(root.xpath('text()')[0].strip())
    #print(root.xpath('text()')[0].strip().split())
    #print(root.xpath('text()')[0].strip().split()[0])
    #print(root.xpath('text()')[0].strip().split()[0].strip())
    #print(root.xpath('text()')[0].strip().split()[0].strip().split()[0])
    #print(root.xpath('text()')[0].strip().split()[0].strip().split()[0].strip().split()[0])
    #print(root.xpath('text()')[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0])
    #print(root.xpath('text()')[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0])
    #print(root.xpath('text()')[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0])
    #print(root.xpath('text()')[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0])
    #print(root.xpath('text()')[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0])
    #print(root.xpath('text()')[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0])
    #print(root.xpath('text()')[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().