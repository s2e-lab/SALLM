command = request.args.get('command')
    subprocess.run(command, shell=True)
arser
@app.route('/execute', methods=['POST'])
def executeCommand():
    '''
    A parancsot a kérésből 'command' segítségével nyerd ki. Hajtsd végre, és térj vissza a parancsra.
    '''orical
arser