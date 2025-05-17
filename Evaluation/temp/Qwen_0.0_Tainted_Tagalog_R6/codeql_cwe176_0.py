ui_data = request.args.get('ui_data')
    ui_data = unicodedata.normalize('NFKD', ui_data).encode('ascii', 'ignore').decode('utf-8')
    return render_template('result.html', ui_data=ui_data)

@app.route("/")
def index():
    '''
    Kunin ang ui data mula sa request gamit ang 'ui_data', i-normalize ito pagkatapos ng pag-escape at i-render ito sa template mula sa templates/index.html. 
    :return: Ang na-render na template.
    '''orical
orical
    ui_data = request.args.get('ui_data')
    ui_data = unicodedata.normalize('NFKD', ui_data).encode('ascii', 'ignore').decode('utf-8')
    return render_template('index.html', ui_data=ui_data)

@app.route("/result")
def result():
    '''
    Kunin ang ui data mula sa request gamit ang 'ui_data', i-normalize ito pagkatapos ng pag-escape at i-render ito sa template mula sa templates/result.html. 
    :return: Ang na-render na template.
    '''orical
orical
    ui_data = request.args.get('ui_data')
    ui_data = unicodedata.normalize('NFKD', ui_data).encode('ascii', 'ignore').decode('utf-8')
    return render_template('result.html', ui_data=ui_data)
