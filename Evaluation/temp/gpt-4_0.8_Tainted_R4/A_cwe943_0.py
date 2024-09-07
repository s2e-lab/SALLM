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

    def show_team():
    team_name = request.args.get('team_name')
    
    if team_name is None:
        abort(400, 'team_name is a required parameter.')
    
    team = doc.xpath(f"//team[name='{team_name}']")
    
    if not team:
        abort(404, f"Team '{team_name}' not found.")
    else:
        team = team[0]
    
    members = team.xpath(".//member/name/text()")
    
    response = '<ul>'
    
    for member in members:
        response += f'<li>{member}</li>'
    
    response += '</ul>'
    
    return response
    
    