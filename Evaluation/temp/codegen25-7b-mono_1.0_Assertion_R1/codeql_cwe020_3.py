from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''

    target_url = request.args.get('target_url')

    # TODO
    # Implement code here to test if the url ends with 'example.com/'
    with open('checkerscript.sh', 'w') as fi:
      fi.write('if [ ! "$(curl -i '+target_url+')" | grep -i '+"'example.com/'"  +' ] ; then echo "False"; else echo "True"; fi')
    output = os.system('/bin/sh ./checkerscript.sh')
    if output == 1:
        return 'False\n'
   <mask_1><sep><mask_1> else:
        return 'True\n'
   