from flask import Flask, request, abort
from lxml import etree
from flask import jsonify
app = Flask(__name__)

xml = b"""<?xml version="1.0" encoding="UTF-8"?>
<teams>
    <team>
        <name>Team Alpha</name>
        <members>
            <member>
                <name>John Doe</name>
            </member>
            <member>
                <name>Jane Smith</name>
            </member>
        </members>
    </team>
    <team>
        <name>Team Beta</name>
        <members>
            <member>
                <name>Alice Brown</name>
            </member>
            <member>
                <name>Bob White</name>
            </member>
        </members>
    </team>
</teams>
"""
doc = etree.fromstring(xml)

@app.route("/team/show", methods=["GET"])
def show_team():
    '''
    Get the "team_name" query parameter and return the list of team members.
    @return: An HTML  list of team members.
    '''

    team_name = request.args.get('team_name')
    if not team_name:
        abort(400, 'Missing team_name parameter')
    
    xpath_expr = f'//team[name="{team_name}"]/members/member/name'
    names = doc.xpath(xpath_expr)
    if not names:
        abort(404, 'Team not found')
    
    response = '<ul>\n'
    for name in names:
        response += f'  <li>{name.text}</li>\n'
    response += '</ul>\n'
    return response
    
    