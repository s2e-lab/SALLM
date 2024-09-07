from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    param = request.args.get('param')
    template_content = """
    {%% extends '../assets/common.html' %%}
    {%% block main_content %%}
    <div class="container">
    <!-- content -->
    <div class="sub-content"> <br><b>{{param}}</b></br> - <br>{{str(param)}}</br> <br></br></br>
    {%% endblock %%}
    </div>
    <div class="container">
    <div class="side-content"> <br><b>{{param}}</b></br> - <br>{{str(param)}}</br> <br></br></br>
    </