from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

# create a dictionary to contain mappings of path to file names
# path keys are path names on the server and the file names are what they should be
# add more file paths to this mapping if you need more file urls
file_maps = {
    'files/': 'textfile.txt',
    'images/': 'pic.jpg',
    'audio/':'music.mp3',
    'documents/': 'docs.txt',
}

file_name = request.args.get("file_name", "") # request file name from the request

# use a regex to filter out characters that aren’t characters.
file_name = re.findall("\D", file_name)

# convert file_name and the keys of file_maps to strings
file_name