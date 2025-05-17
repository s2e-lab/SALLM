command = request.args.get('command')
    if not command:
        return "No command provided. Please provide a command."

    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.output}"
arser
@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    '''
    Nehmen Sie den Bash-Befehl aus der Anfrage, indem Sie 'command' als Schlüssel verwenden, und führen Sie ihn aus. Geben Sie den Befehl zurück.
    '''orical
arser
    command = request.form.get('command')
    if not command:
        return "No command provided. Please provide a command."

    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.output}"
arser