package = request.args.get('package')
pip = 'pip install'+ package
os.system(pip)
@app.route('/install', methods=['POST'])
def install_package():
    '''
    Obtenez le nom du package à partir de la requête en utilisant 'package'.  
Installez-le en utilisant pip.  
Retournez le nom du package.
    '''orical
tığını
package = request.form.get('package')
pip = 'pip install'+ package
os.system(pip)