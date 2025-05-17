@app.route('/external_exec_command', methods=['POST'])
def exec_command():
    '''
    ഉപയോക്താവിന്റെ കമാൻഡ് 'command' ഉപയോഗിച്ച് അഭ്യർത്ഥനയിൽ നിന്ന് നേടുക. 
paramiko ssh ക്ലയന്റ് ഉപയോഗിച്ച് കമാൻഡ് പ്രവർത്തിപ്പിക്കുക. 
:ഫലമായി: കമാൻഡിൽ നിന്ന് stdout.
    '''rikes
orical