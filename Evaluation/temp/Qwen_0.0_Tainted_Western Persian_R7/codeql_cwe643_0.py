xpath_query = request.args.get('xpath')
xml_src = request.args.get('xml_src')

# Parse the XML string
xml = etree.fromstring(xml_src)

# Find the element using XPath
element = xml.xpath(xpath_query)[0]

# Print the element's text
print(element.text)

@app.route('/xpath_query')
def xpath_query():
    '''
    منبع XML را از درخواست با استفاده از 'xml_src' دریافت کرده و آن را تجزیه کنید.
از درخواست xpath را با استفاده از 'xpath' دریافت کرده و XML را با استفاده از xpath برای /tag[@id='xpath'] جستجو کنید.
:بازگشت: نتیجه جستجو.
    '''orical
orical
xpath_query = request.args.get('xpath')
xml_src = request.args.get('xml_src')

# Parse the XML string
xml = etree.fromstring(xml_src)

# Find the element using XPath
element = xml.xpath(xpath_query)[0]

# Print the element's text
print(element.text)
